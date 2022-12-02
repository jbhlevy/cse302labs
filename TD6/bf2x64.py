#! /usr/bin/env python3


import os
import sys

from brainfuck import BFBackward, BFDecrement, BFExit, BFForward, BFIncrement, BFInstruction, BFMemory, BFPrint


class Instruction:
    def __init__(self, offset : int, arithmetic, p=False):
        self.offset = offset
        self.arithmetic = abs(arithmetic)
        if arithmetic < 0:
            self.operator = '-='
        elif arithmetic >= 0 and not p:
            self.operator = '+='
        if arithmetic == 0 and p:
            self.operator = "print"

    def __str__(self):
        if self.operator == "print":
            return f"print data[{self.offset}]"
        else:
            return f"data[{self.offset}] {self.operator} {self.arithmetic}"

    def __repr__(self) -> str:
        if self.operator == "print":
            return f"print data[{self.offset}]"
        else:
            return f"data[{self.offset}] {self.operator} {self.arithmetic}"


def translate(program : list):
    print(f"Program is {program}")
    index = 0
    instr_list = []
    curr_instr = program[0]
    offset_buffer = 0
    arithmetic_buffer = 0 #init(curr_instr)

    while(index != len(program)):
        curr_instr = program[index]
        if index != len(program)-1:
            next_instr = program[index+1]
        if is_incr(curr_instr):
            arithmetic_buffer = arithmetic_buffer + 1 if isinstance(curr_instr, BFIncrement) else arithmetic_buffer - 1
            if is_ptr(next_instr) or is_print(next_instr):
                emit(instr_list, offset_buffer, arithmetic_buffer)
                arithmetic_buffer = 0
        elif is_ptr(curr_instr):
            offset_buffer = offset_buffer + 1 if isinstance(curr_instr, BFForward) else offset_buffer -1
        elif is_print(curr_instr):
            emit(instr_list, offset_buffer, arithmetic_buffer, True)
        
        curr_instr = next_instr
        index += 1
        print(offset_buffer, arithmetic_buffer)

    if is_ptr(curr_instr):
        emit(instr_list, offset_buffer, arithmetic_buffer)

    return instr_list, offset_buffer

def emit(instr_list, offset, arithmetic, p=False):
    instr_list.append(Instruction(offset, arithmetic, p))

def init(instruction):
    if is_ptr(instruction):
        if isinstance(instruction, BFForward):
            return (1, 0)
        else:
            return (-1, 0)
    else:
        if isinstance(instruction, BFIncrement):
            return (0, 1)
        else:
            return (0, -1)

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



def to_asm(instructions : list):
    print('tets', instructions[0].offset)
    asm = []
    asm.extend([f"\t.bss", 
                f"buffer:", 
                f"\t.zero 30000\n", 
                f"\t.text", 
                f"\t.globl main", 
                f"main:"
    ])
    current_offset = 0
    for instruction in instructions:
        print("instrucion : ", instruction.offset)
        if current_offset + instruction.offset < 0:
            current_offset = 30000 + instruction.offset
        elif current_offset + instruction.offset > 30000:
            current_offset = 30000 - (current_offset + instruction.offset)

        cell = f"(buffer+{instruction.offset})(%rip)"
        if instruction.operator == "+=":
            asm.extend([f"\t xor %al, %al",
                        f"\t mov {cell}, %al", 
                        #f"\t movq %rax, %rdi",
                        #f"\t call bf_print",
                        #f"\t xorq %rdi, %rdi",
                        f"\t add ${instruction.arithmetic}, %al",
                        #f"\t movq %rax, %rdi", 
                        #f"\t callq bf_print",
                        f"\t mov %al, {cell}"])
            pass
        elif instruction.operator == "-=":
            asm.extend([f"\t mov {cell}, %al", 
                        f"\t sub ${instruction.arithmetic}, %al",
                        f"\t mov %al, {cell}"])
        elif instruction.operator == "print":
            asm.extend([f"\t xor %dil, %dil",
                        f"\t mov {cell}, %dil",
                        f"\t call bf_print"])
    

    asm.extend([f"\tretq"])

    return asm







            





def _main():
    if len(sys.argv)-1 != 1:
        print(f'Usage: {sys.argv[0]} [FILE.bf]', file = sys.stderr)
        exit(1)

    with open(sys.argv[1]) as stream:
        program = stream.read()
    program = BFInstruction.parse(program)

    print(program)
    intermediate, current_offset = translate(program.block)
    print(intermediate, current_offset)
    print('main', intermediate[0].offset)
    asm = to_asm(intermediate)
    print("ASM GENERATION\n =========")
    for l in asm:
        print(l)
    print(" ========= \nASM GENERATION")   
    assembly_name = sys.argv[1][:-2] + "s"
    print(assembly_name)
    with open(assembly_name, 'w') as fn:
        print(*asm, file=fn, sep='\n')

    shell_command = f"gcc -o {sys.argv[1][:-3]} {assembly_name} bf_runtime.c"
    gcc_stat = os.system(shell_command)
    if not (os.WIFEXITED(gcc_stat) and os.WEXITSTATUS(gcc_stat) == 0):
        print(f'gcc exited abnormally')

    cleanup = f"rm {assembly_name}"
    os.system(cleanup)

    # try:
    #     program.execute(BFMemory())
    # except BFExit:
    #    pass

# --------------------------------------------------------------------
if __name__ == '__main__':
    _main()