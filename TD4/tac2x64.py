#!/usr/bin/env python3

"""
This is a very simple TAC to x64 assembly pass. It only handles straightline
code and a single main() function.

Usage: python3 tac2asm.py tacfile.json
Produces: tacfile.s (assembly) and tacfile.exe (executable)
Requires: a working gcc
"""

from cgitb import reset
import json
from bx2tac import Instruction
from typing import List
import sys
import os


jcc = {"je": (lambda arg, label: ['movq $0, %r11',
                                    f'cmpq %r11, {arg}',
                                    f'je {label}']),
        "jnz": (lambda arg, label: ['movq $0, %r11',
                                    f'cmpq %r11, {arg}',
                                    f'jne {label}']),
        "jl": (lambda arg, label: ['movq $0, %r11',
                                    f'cmpq %r11, {arg}',
                                    f'jl {label}']),
        "jle": (lambda arg, label: ['movq $0, %r11',
                                    f'cmpq %r11, {arg}',
                                    f'jle {label}']),
        "jg": (lambda arg, label: ['movq $0, %r11',
                                    f'cmpq %r11, {arg}',
                                    f'jg {label}']),
        "jge": (lambda arg, label: ['movq $0, %r11',
                                        f'cmpq %r11, {arg}',
                                        f'jge {label}'])
        }


binops = {'add': 'addq',
            'sub': 'subq',
            'mul': (lambda ra, rb, rd: [f'movq {ra}, %rax',
                                        f'imulq {rb}',
                                        f'movq %rax, {rd}']),
            'div': (lambda ra, rb, rd: [f'movq {ra}, %rax',
                                        f'cqto',
                                        f'idivq {rb}',
                                        f'movq %rax, {rd}']),
            'mod': (lambda ra, rb, rd: [f'movq {ra}, %rax',
                                        f'cqto',
                                        f'idivq {rb}',
                                        f'movq %rdx, {rd}']),
            'and': 'andq',
            'or': 'orq',
            'xor': 'xorq',
            'shl': (lambda ra, rb, rd: [f'movq {ra}, %r11',
                                        f'movq {rb}, %rcx',
                                        f'salq %cl, %r11',
                                        f'movq %r11, {rd}']),
            'shr': (lambda ra, rb, rd: [f'movq {ra}, %r11',
                                        f'movq {rb}, %rcx',
                                        f'sarq %cl, %r11',
                                        f'movq %r11, {rd}'])}
unops = {'neg': 'negq',
            'not': 'notq'}

param_map = [
        f'%rdi',
        f'%rsi',
        f'%rdx',
        f'%rcx',
        f'%r8',
        f'%r9']

def lookup_temp(var, temp_map, gvars, args, stack_size):
    print("Reached lookup function", args)
    if var in gvars:
        return (temp_map, stack_size, f"{var[1:]}(%rip)")
    elif var in args:
        print("Branch 2:", args.index(var))
        if args.index(var) >= 6:
            print("Condition checked")
            return (temp_map, stack_size, f"{16+8*(args.index(var)-6)}(%rbp)")
        else:
            if var not in temp_map:
                stack_size += 1
                temp_map[var] = f"{-8*stack_size}(%rbp)"
            return (temp_map, stack_size, temp_map[var])

    else:
        if var not in temp_map:
            stack_size += 1
            temp_map[var] = f"{-8*stack_size}(%rbp)"
        return (temp_map, stack_size, temp_map[var])


    # def lookup_temp(self, temp, temp_map):
    #     assert (isinstance(temp, str)) #and
    #     # temp[0] == '%'), temp
    #     if temp[0] == "@":
    #         temp = temp[1:]
    #     # assert (isinstance(temp, str) and
    #     #         temp[0] == '%' and
    #     #         temp[1:].isnumeric()), temp
    #     #returns the value of temp
    #     return temp_map.setdefault(temp, f'{-8 * (len(temp_map) + 1)}(%rbp)')

def tac_to_asm(tac_instrs, gvars, name, proc_args, temp_map, stack_size):
        """
        Get the x64 instructions correspondign to the TAC instructions
        """
        print(proc_args)
        asm = []
        if proc_args != []:
            print("Procedure has arguments")
            for i in range(min(len(proc_args), 6)):
                print(proc_args[i])
                temp_map, stack_size, res = lookup_temp(proc_args[i], temp_map, gvars, proc_args, stack_size)
                asm.append(f"\tmovq {param_map[i]}, {res}")

        for instr in tac_instrs:
            print(instr)
            opcode = instr.opcode
            args = instr.args
            result = instr.result
            if opcode == 'nop':
                pass
            elif opcode == 'const':
                assert len(args) == 2 and isinstance(args[0], int) or len(args) == 1
                temp_map, stack_size, res = lookup_temp(result, temp_map, gvars, proc_args, stack_size)
                asm.append(f'movq ${args[0]}, {res}')
            elif opcode == 'label':
                assert (len(args) == 2 or len(args) == 1)
                #Changes above assertion because of tac_cfoot.py
                asm.append(f'{args[0][1:]}:')
            elif opcode == 'jmp':
                print("jmp arg",args[0][1:])
                assert (len(args) == 2 or len(args) == 1)
                #Changes above assertion because of tac_cfoot.py
                asm.append(f'jmp {args[0][1:]}')
            elif opcode in jcc:
                assert len(args) == 2
                assert result == None
                temp_map, stack_size, arg1 = lookup_temp(args[0], temp_map, gvars, proc_args, stack_size)
                asm.extend([f'\tmovq {arg1}, %r11', f'\tcmpq $0, %r11', f'\t{opcode} {args[1][1:]}'])
            elif opcode == 'copy':
                #Made modif form len = 1 to len = 2 because of tac_cfoot.py
                assert len(args) == 2 or len(args) == 1
                temp_map, stack_size, arg = lookup_temp(args[0], temp_map, gvars, proc_args, stack_size)
                temp_map, stack_size, res = lookup_temp(result, temp_map, gvars, proc_args, stack_size)
                asm.append(f'movq {arg}, %r11')
                asm.append(f'movq %r11, {res}')
            elif opcode in binops:
                assert len(args) == 2
                temp_map, stack_size, arg1 = lookup_temp(args[0], temp_map, gvars, proc_args, stack_size)
                temp_map, stack_size, arg2 = lookup_temp(args[1], temp_map, gvars, proc_args, stack_size)
                temp_map, stack_size, res = lookup_temp(result, temp_map, gvars, proc_args, stack_size)
                proc = binops[opcode]
                if isinstance(proc, str):
                    asm.extend([f'movq {arg1}, %r11',
                                f'{proc} {arg2}, %r11',
                                f'movq %r11, {res}'])
                else:
                    asm.extend(proc(arg1, arg2, res))
            elif opcode in unops:
                assert len(args) == 2 or len(args) == 1
                temp_map, stack_size, arg = lookup_temp(args[0], temp_map, gvars, proc_args, stack_size)
                temp_map, stack_size, res = lookup_temp(result, temp_map, gvars, proc_args, stack_size)
                proc = unops[opcode]
                asm.extend([f'movq {arg}, %r11',
                            f'{proc} %r11',
                            f'movq %r11, {res}'])
            # elif opcode == 'print':
            #     assert len(args) == 1
            #     assert result == None
            #     arg = self.lookup_temp(args[0], temp_map)
            #     asm.extend(["pushq %rdi",
            #                 "pushq %rax",
            #                 f'movq {arg}, %rdi',
            #                 "callq bx_print_int",
            #                 "popq %rax",
            #                 "popq %rdi"])
            elif opcode == 'ret':
                if args == []:
                    asm.extend(["\txorq %rax, %rax", f"\tjmp .Lend_{name}"])
                else:
                    temp_map, stack_size, arg = lookup_temp(args[0], temp_map, gvars, proc_args, stack_size)
                    asm.extend([f"\tmovq {arg}, %rax", f"\tjmp .Lend_{name}"])
            elif opcode == "param":
                temp_map, stack_size, arg = lookup_temp(
                args[1], temp_map, gvars, proc_args, stack_size)
                if args[0] <= 6:
                    res = param_map[args[0]-1]
                    asm.append(f"\tmovq {arg}, {res}")
                else:
                    asm.append(f"\tpushq {arg}")

            elif opcode == "call":
                #arg = self.lookup_temp(args[0], temp_map)
                asm.append(f"\tcallq {args[0][1:]}")
                if result != '%_':
                    temp_map, stack_size, res = lookup_temp(result, temp_map, gvars, proc_args, stack_size)
                    asm.append(f"\tmovq %rax, {res}")
            else:
                assert False, f'unknown opcode: {opcode}'

        stack_size = len(temp_map)
        if stack_size % 2 != 0:
            stack_size += 1
        asm = [f"\t.globl {name}", "\t.text", f"{name}:", "\tpushq %rbp",
                "\tmovq %rsp, %rbp", f"\tsubq ${8*stack_size}, %rsp"] + asm

        if name == 'main':
            asm.append("\txorq %rax, %rax")

        asm += [f".Lend_{name}:", "\tmovq %rbp, %rsp",
                "\tpopq %rbp", "\tretq", "", ]

        return asm, temp_map, stack_size


        # asm[:0] = [f'pushq %rbp',
        #         f'movq %rsp, %rbp',
        #         f'subq ${8 * len(temp_map)}, %rsp']
        # asm.extend([f'movq %rbp, %rsp',
        #             f'popq %rbp',
        #             f'xorq %rax, %rax',
        #             f'retq'])
        return asm



#what is going on here
#j'ai fait une autre version de compile_tac en dessous, au cas ou
# def compile_tac(tjs):
#     assert isinstance(tjs, list), tjs
#     asm_decl = []
#     asm_proc = []
#     for cu in tjs:
#         if "var" in cu.keys():
#             asm_decl += [f'\t.globl {cu["var"][1:]}', 
#                         f'\t.data',
#                         f'{cu["var"][1:]}:\t.quad {cu["init"]}'
#                         ]

#             #Global Var declaration 
#         elif "proc" in cu.keys():
#             instr_list = [Instruction(tmp["opcode"], tmp["args"], tmp["result"]) for tmp in cu["body"]]
#             print(instr_list)
#             x64CU = X64CU(instr_list)
#             if cu["proc"] != "@main":
#                 print(cu["proc"])

#                 asm_proc += ['\t' + line for line in x64CU.tac_to_asm()]
#                 asm_proc[:0] = [f'\t.globl {cu["proc"][1:]}', 
#                                 f'\t.text', 
#                                 f'{cu["proc"][1:]}:'
#                                 ]
#             else:
#                 asm_main = ['\t' + line for line in x64CU.tac_to_asm()]
#                 asm_main[:0] = [f'\t.section .rodata',
#                            f'.lprintfmt:',
#                            f'\t.string "%ld\\n"',
#                            f'\t.text',
#                            f'\t.globl main',
#                            f'main:']


#         else: 
#             raise KeyError("Unsupported compilation unit, needs to be proc or var")

#     asm = asm_main + asm_decl + asm_proc
#    return asm


def compile_tac(fname):
    tjs = None
    with open(fname, 'rb') as fp:
        tjs = json.load(fp)
    assert isinstance(tjs, list), tjs

    gvars = []
    asm = []
    stack = dict()
    stack_size = 0

    # gvars
    for decl in tjs:
        if 'var' in decl:
            name = decl['var']
            value = decl['init']
            gvars.append(name)
            asm.extend([f"\t.globl {name[1:]}",
                        "\t.data",
                        f"{name[1:]}: .quad {value}"])

    # procs decs
    for decl in tjs:
        if 'proc' in decl:
            name = decl['proc']
            args = decl['args']
            body = [Instruction(instr["opcode"], instr["args"], instr["result"]) for instr in decl['body']]
            print("args of proc", args)
            proc_asm, stack, stack_size = tac_to_asm(
                body, gvars, name[1:], args, stack, stack_size)
            asm.extend(proc_asm)

    with open(fname[:-9] + '.s', 'w') as fn:
        print(*asm, file=fn, sep='\n')
    return fname[:-9] + '.s'