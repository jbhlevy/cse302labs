#! /usr/bin/env python3

import argparse
import os
import sys

from brainfuck import BFBackward, BFDecrement, BFExit, BFForward, BFIncrement, BFInput, BFInstruction, BFLoop, BFMemory, BFPrint

#Classes for Intermediate representation

class Instruction:
    def __init__(self, offset: int):
        self.offset = offset
        
class Arithmetic(Instruction):
    def __init__(self, offset : int, arithmetic):
        self.offset = offset
        self.arithmetic = abs(arithmetic)
        if arithmetic < 0:
            self.operator = '-'
        elif arithmetic >= 0:
            self.operator = '+'

class Pointer(Instruction):
    def __init__(self, offset: int):
        self.offset = offset
        self.operator = 'move'

class Input(Instruction):
    def __init__(self):
        self.offset = None
        self.operator = "input"

class Print(Instruction):
    def __init__(self):
        self.offset = None
        self.operator = "print"

class Loop:
    def __init__(self, offset : int, body : list) -> None:
        self.offset = None
        self.operator = "loop"
        self.body = body
        self.scan_loop = False
        self.f = None

#---------------------------------------------------------------------------
#Translation to IR 

def translate_instr(program : list, offset=0):
    index = 0
    instr_list = []
    curr_instr = program[0]
    offset_buffer = offset
    arithmetic_buffer = 0

    while(index != len(program)):
        curr_instr = program[index]
        if index != len(program)-1:
            next_instr = program[index+1]
        else: next_instr = None

        if is_incr(curr_instr):
            arithmetic_buffer = arithmetic_buffer + 1 if isinstance(curr_instr, BFIncrement) else arithmetic_buffer - 1
            if is_ptr(next_instr) or is_print(next_instr) or is_loop(next_instr) or index == len(program)-1:
                emit(instr_list, offset_buffer, arithmetic_buffer)
                emit_ptr(instr_list, offset_buffer)
                arithmetic_buffer = 0
                offset_buffer = 0
        elif is_ptr(curr_instr):
            tmp = offset_buffer
            offset_buffer = offset_buffer + 1 if isinstance(curr_instr, BFForward) else offset_buffer -1
            if is_loop(next_instr) or index == len(program)-1 or is_print(next_instr):
                emit_ptr(instr_list, offset_buffer)
                offset_buffer = 0
        elif is_print(curr_instr):
            emit_print(instr_list, offset_buffer)
        elif is_loop(curr_instr):
            body, off = translate_instr(curr_instr.body.block, offset_buffer) # Translate body into list of instructions just as before 
            emit_loop(instr_list, offset_buffer, body)
        elif is_input(curr_instr):
            emit_input(instr_list, offset_buffer)
        index += 1
    return instr_list, offset_buffer

def emit(instr_list, offset, arithmetic):
    instr_list.append(Arithmetic(offset, arithmetic))

def emit_ptr(instr_list, offset):
    instr_list.append(Pointer(offset))

def emit_loop(instr_list, offset, body):
    instr_list.append(Loop(offset, body))

def emit_input(instr_list, offset):
    instr_list.append(Input())

def emit_print(instr_list, offset):
    instr_list.append(Print())

def is_ptr(instruction):
    if isinstance(instruction, BFBackward) or isinstance(instruction, BFForward):
        return True
    else: 
        return False

def is_incr(instruction):
    if isinstance(instruction, BFDecrement) or isinstance(instruction, BFIncrement):
        return True
    else: 
        return False
def is_print(instruction):
    if isinstance(instruction, BFPrint):
        return True
    else:
        return False

def is_loop(instruction):
    if isinstance(instruction, BFLoop):
        return True 
    else:
        return False
def is_input(instruction):
    if isinstance(instruction, BFInput):
        return True 
    else:
        return False
        
#-----------------------------------------------------------------------------------------------------
#Optimization 


def scan_loop_opt(instructions : list):
    index = 0
    tmp = []
    while(index != len(instructions)):
        curr_instr = instructions[index]
        if isinstance(curr_instr, Loop) and isinstance(curr_instr.body[0], Pointer):
            curr_instr.scan_loop = True
            if curr_instr.body[0].offset == 1:
                curr_instr.f = True
            elif curr_instr.body[0].offset == -1:
                curr_instr.f = False
        tmp.append(curr_instr)
        index += 1
    return tmp

def optimize(prog : list):
    return scan_loop_opt(prog)
    
#-----------------------------------------------------------------------------------------------------
#Translation to x64

def to_asm(instructions : list, last_label =0, offset = 0):
    ptr = f"%r15"
    asm = []
    if last_label == 0:
        asm.extend([f"\t.bss", 
                    f"buffer:", 
                    f"\t.zero 30000\n", 
                    f"\t.text", 
                    f"\t.globl main", 
                    f"main:", 
                    f"\t pushq %rbp", 
                    f"\t movq %rsp, %rbp", 
                    f"\t leaq buffer(%rip), {ptr}"])
    current_offset = offset
    for instruction in instructions:
        current_offset = instruction.offset if instruction.offset is not None else current_offset
        #print(instruction, ":", instruction.offset)
        #print("curr", current_offset)
        cell = f"{current_offset}({ptr})" if current_offset != 0 else f"({ptr})"


        if instruction.operator == "+":
            asm.extend([f"\t addb ${instruction.arithmetic}, {cell}"
            ])
        elif instruction.operator == "-":
            asm.extend([f"\t subb ${instruction.arithmetic}, {cell}"])
        elif instruction.operator == "print":
            asm.extend([f"\t xor %dil, %dil",
                        f"\t movb ({ptr}), %dil",
                        f"\t callq putchar"])
        elif instruction.operator == "input":
            asm.extend([f"\t xor %al, %al",
                        f"\t callq getchar", 
                        f"\t mov %al, ({ptr})"])

        elif instruction.operator == "move":
            asm.extend([f"\t addq ${instruction.offset}, {ptr}"])

        elif instruction.operator == "loop":

            if instruction.scan_loop:
                asm.extend([f"\t leaq buffer(%rip), %r11", 
                            f"\t movq {ptr}, %r10", 
                            f"\t movq %r11, %r9", 
                            f"\t addq $29999, %r9"])
                if instruction.f:
                    asm.extend([f"\t movq %r10, %rdi", 
                                f"\t movb $0, %sil"
                                f"\t movq %r9, %r8", 
                                f"\t subq %r10, %r8", 
                                f"\t movq %r8, %rdx",
                                f"\t callq memchr"])
                else:
                    asm.extend([f"\t movq %r11, %rdi",
                                f"\t movb $0, %sil",
                                f"\t movq %r10, %r8", 
                                f"\t subq %r11, %r8", 
                                f"\t movq %r8, %rdx",
                                f"\t callq memrchr"])
                asm.extend([f"\t movq %rax, {ptr}"])
            else:
                last_label +=1
                l_entry = f".L{last_label}"
                last_label +=1
                l_out = f".L{last_label}"
                asm.extend([f"{l_entry}:", 
                            f"\t cmpb $0, ({ptr})",
                            f"\t je {l_out}"])
                #print("entering recursion", current_offset)
                body, label_offset = to_asm(instruction.body, last_label, current_offset)
                #print("exited recursions")
                asm.extend(body)
                asm.extend([f"\t jmp {l_entry}"])
                asm.extend([f"{l_out}:"])
                last_label = label_offset
 
    return asm, last_label

#-----------------------------------------------------------------------------------------------------
#Driver Code

def _main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-o', dest = 'save_asm', action='store_true', default=False, help= 'Save the generated asm into a .s file')
    ap.add_argument('-v', dest = 'verbosity', action='store_true', default=False, help= 'Show debuging information')
    ap.add_argument('-c', dest = 'compile', action='store_true', default=False, help="run the compiler to create an executable file")
    ap.add_argument('fname',metavar='FILE', type=str, nargs=1, help='The BF file to compile')

    options = ap.parse_args(sys.argv[1:])

    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} [-o] [-v] [-c] [FILE.bf]', file = sys.stderr)
        exit(1)
    
    bf_filename = options.fname[0]
    if not bf_filename.endswith('.bf'):
        print(f'File {bf_filename} does not have .bf extension')
        sys.exit(1)

    with open(bf_filename) as stream:
        program = stream.read()
    program = BFInstruction.parse(program)

    if(options.verbosity):
        print(f"After parsing by brainfuck.py the obtained object is: {program}")


    intermediate, current_offset = translate_instr(program.block)

    #intermediate = optimize(intermediate)

    if(options.verbosity):
        print(f"After translation to intermediate representation & optimization, the list of instructions is: {intermediate}, the data pointer will be changed by {current_offset}")
    
    asm, tmp = to_asm(intermediate)

    asm.extend([f"\t xorq %rax, %rax", 
                f"\t movq %rbp, %rsp", 
                f"\t popq %rbp",
                f"\t retq"]) 

    if(not options.save_asm):
        print(f"ASM GENERATION\n=============")
        for l in asm:
            print(l)
        print("=============\nEND OF ASM GENERATION")

    assembly_name = bf_filename[:-2] + "s"
    with open(assembly_name, 'w') as fn:
        print(*asm, file=fn, sep='\n')
    
    print(f"{bf_filename} -> {assembly_name}")



    if (options.compile):
        shell_command = f"gcc -o {assembly_name[:-2]} {assembly_name} "
        gcc_stat = os.system(shell_command)
        if not (os.WIFEXITED(gcc_stat) and os.WEXITSTATUS(gcc_stat) == 0):
            print(f'ERROR: gcc exited abnormally')

    if (not options.save_asm):
        cleanup = f"rm {assembly_name}"
        os.system(cleanup)

# --------------------------------------------------------------------
if __name__ == '__main__':
    _main()