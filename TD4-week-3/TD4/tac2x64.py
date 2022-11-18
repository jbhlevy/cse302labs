#!/usr/bin/env python3

"""
This is a very simple TAC to x64 assembly pass. It only handles straightline
code and a single main() function.

Usage: python3 tac2asm.py tacfile.json
Produces: tacfile.s (assembly) and tacfile.exe (executable)
Requires: a working gcc
"""

import json
from ast2tac import Instruction
from typing import List
import sys
import os

class X64CU:
    def __init__(self, tac_instr) -> None:
        self.instr_list = tac_instr


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


    def lookup_temp(self, temp, temp_map):
        assert (isinstance(temp, str) and
        temp[0] == '%'), temp
        # assert (isinstance(temp, str) and
        #         temp[0] == '%' and
        #         temp[1:].isnumeric()), temp
        #returns the value of temp
        return temp_map.setdefault(temp, f'{-8 * (len(temp_map) + 1)}(%rbp)')

    def tac_to_asm(self):
        """
        Get the x64 instructions correspondign to the TAC instructions
        """
        tac_instrs = self.instr_list
        temp_map = dict()
        asm = []
        for instr in tac_instrs:
            opcode = instr.opcode
            args = instr.args
            result = instr.result
            if opcode == 'nop':
                pass
            elif opcode == 'const':
                assert len(args) == 1 and isinstance(args[0], int)
                result = self.lookup_temp(result, temp_map)
                asm.append(f'movq ${args[0]}, {result}')
            elif opcode == 'label':
                assert len(args) == 1
                asm.append(f'{args[0][1:]}:')
            elif opcode == 'jmp':
                assert len(args) == 1
                asm.append(f'jmp {args[0][1:]}')
            elif opcode in X64CU.jcc:
                jump = X64CU.jcc[opcode]
                assert len(args) == 2
                arg = self.lookup_temp(args[0], temp_map)
                label = args[1][1:]
                #adds to the end of asm
                asm.extend(jump(arg, label))
            elif opcode == 'copy':
                assert len(args) == 1
                arg = self.lookup_temp(args[0], temp_map)
                result = self.lookup_temp(result, temp_map)
                asm.append(f'movq {arg}, %r11')
                asm.append(f'movq %r11, {result}')
            elif opcode in X64CU.binops:
                assert len(args) == 2
                arg1 = self.lookup_temp(args[0], temp_map)
                arg2 = self.lookup_temp(args[1], temp_map)
                result = self.lookup_temp(result, temp_map)
                proc = X64CU.binops[opcode]
                if isinstance(proc, str):
                    asm.extend([f'movq {arg1}, %r11',
                                f'{proc} {arg2}, %r11',
                                f'movq %r11, {result}'])
                else:
                    asm.extend(proc(arg1, arg2, result))
            elif opcode in X64CU.unops:
                assert len(args) == 1
                arg = self.lookup_temp(args[0], temp_map)
                result = self.lookup_temp(result, temp_map)
                proc = X64CU.unops[opcode]
                asm.extend([f'movq {arg}, %r11',
                            f'{proc} %r11',
                            f'movq %r11, {result}'])
            elif opcode == 'print':
                assert len(args) == 1
                assert result == None
                arg = self.lookup_temp(args[0], temp_map)
                asm.extend(["pushq %rdi",
                            "pushq %rax",
                            f'movq {arg}, %rdi',
                            "callq bx_print_int",
                            "popq %rax",
                            "popq %rdi"])
            elif opcode == 'ret':
                assert result == None 
                if len(args) == 1: 
                    arg = self.lookup_temp(args[0], temp_map)
                    asm.extend([f'movq %rbp, %rsp',
                                f'popq %rbp',
                                f"movq {arg}, %rax"])
                elif len(args) == 0: 
                    asm.extend([f'movq %rbp, %rsp',
                                f'popq %rbp',
                                f"xorq %rax, %rax"])

                else:
                    Exception("Bad return args ")

                asm.extend([])
            else:
                assert False, f'unknown opcode: {opcode}'
        asm[:0] = [f'pushq %rbp',
                f'movq %rsp, %rbp',
                f'subq ${8 * len(temp_map)}, %rsp']
        asm.extend([f'movq %rbp, %rsp',
                    f'popq %rbp',
                    f'xorq %rax, %rax',
                    f'retq'])
        return asm

def compile_tac(tjs):
    assert isinstance(tjs, list), tjs
    asm_decl = []
    asm_proc = []
    for cu in tjs:
        if "var" in cu.keys():
            asm_decl += [f'\t.globl {cu["var"][1:]}', 
                        f'\t.data',
                        f'{cu["var"][1:]}:\t.quad {cu["init"]}'
                        ]

            #Global Var declaration 
        elif "proc" in cu.keys():
            if cu["proc"] != "@main":
                print(cu["proc"])
                instr_list = [Instruction(tmp["opcode"], tmp["args"], tmp["result"]) for tmp in cu["body"]]
                print(instr_list)
                x64CU = X64CU(instr_list)

                asm_proc += ['\t' + line for line in x64CU.tac_to_asm()]

                asm_proc[:0] = [f'\t.globl {cu["proc"]}', 
                                f'\t.text', 
                                f'{cu["proc"]}:'
                                ]

        else: 
            raise KeyError("Unsupported compilation unit, needs to be proc or var")

    asm = asm_decl + asm_proc
    # asm += ['\t' + line for line in X64CU.tac_to_asm(instr_list)]
    # asm[:0] = [f'\t.section .rodata',
    #            f'.lprintfmt:',
    #            f'\t.string "%ld\\n"',
    #            f'\t.text',
    #            f'\t.globl main',
    #            f'main:']
    return asm