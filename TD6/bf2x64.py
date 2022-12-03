#! /usr/bin/env python3


import argparse
import os
import sys

from brainfuck import BFBackward, BFDecrement, BFExit, BFForward, BFIncrement, BFInput, BFInstruction, BFLoop, BFMemory, BFPrint

class Instruction:
    def __init__(self, offset : int, arithmetic, p=False):
        self.offset = offset
        self.arithmetic = abs(arithmetic)
        if arithmetic < 0:
            self.operator = '-'
        elif arithmetic >= 0 and not p:
            self.operator = '+'
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

class Input:
    def __init__(self, offset: int):
        self.offset = offset
        self.operator = "input"

    def __repr__(self):
        return f"Current offset : {self.offset}, user input"

class Loop:
    def __init__(self, offset : int, body : list) -> None:
        self.offset = offset
        self.operator = "loop"
        self.body = body

    def __repr__(self):
        return f"Current offset : {self.offset}, adding a {self.operator}"


def translate_instr(program : list, offset=0):
    #print(f"Program is {program}")
    index = 0
    instr_list = []
    curr_instr = program[0]
    offset_buffer = offset
    arithmetic_buffer = 0 #init(curr_instr)

    while(index != len(program)):
        curr_instr = program[index]
        if index != len(program)-1:
            next_instr = program[index+1]
        else: next_instr = None
        if is_incr(curr_instr):
            arithmetic_buffer = arithmetic_buffer + 1 if isinstance(curr_instr, BFIncrement) else arithmetic_buffer - 1
            if is_ptr(next_instr) or is_print(next_instr) or is_loop(next_instr) or index == len(program)-1:
                emit(instr_list, offset_buffer, arithmetic_buffer)
                arithmetic_buffer = 0
            curr_instr = next_instr
        elif is_ptr(curr_instr):
            offset_buffer = offset_buffer + 1 if isinstance(curr_instr, BFForward) else offset_buffer -1
            curr_instr = next_instr
        elif is_print(curr_instr):
            emit(instr_list, offset_buffer, arithmetic_buffer, True)
            curr_instr = next_instr
        elif is_loop(curr_instr):
            body, off = translate_instr(curr_instr.body.block, offset_buffer) # Translate body into list of instructions just as before 
            emit_loop(instr_list, offset_buffer, body)
        elif is_input(curr_instr):
            emit_input(instr_list, offset_buffer)





        #curr_instr = next_instr
        index += 1
        #print(offset_buffer, arithmetic_buffer)

    if is_ptr(curr_instr):
        emit(instr_list, offset_buffer, arithmetic_buffer)

    return instr_list, offset_buffer

def emit(instr_list, offset, arithmetic, p=False):
    instr_list.append(Instruction(offset, arithmetic, p))

def emit_loop(instr_list, offset, body):
    instr_list.append(Loop(offset, body))

def emit_input(instr_list, offset):
    instr_list.append(Input(offset))

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
        

def to_asm(instructions : list, last_label =0):
    #print('tets', instructions[0].offset)
    asm = []
    if last_label == 0:
        asm.extend([f"\t.bss", 
                    f"buffer:", 
                    f"\t.zero 30000\n", 
                    f"\t.text", 
                    f"\t.globl main", 
                    f"main:"
        ])
    current_offset = 0
    for instruction in instructions:
        print(instruction)

        print("instrucion : ", instruction.offset)
        if current_offset + instruction.offset < 0:
            print("back overflow")
            current_offset = 30000 + instruction.offset
            print(current_offset)
        elif current_offset + instruction.offset > 30000:
            print("overflow")
            current_offset = 30000 - (current_offset + instruction.offset)
            print(current_offset)
        # else: 
        #     current_offset = instruction.offset

        cell = f"(buffer+{instruction.offset})(%rip)"

        if instruction.operator == "+":
            asm.extend([f"\t xor %al, %al",
                        f"\t mov {cell}, %al", 
                        f"\t add ${instruction.arithmetic}, %al",
                        f"\t mov %al, {cell}"])
            pass
        elif instruction.operator == "-":
            asm.extend([f"\t mov {cell}, %al", 
                        f"\t sub ${instruction.arithmetic}, %al",
                        f"\t mov %al, {cell}"])
        elif instruction.operator == "print":
            asm.extend([f"\t xor %dil, %dil",
                        f"\t mov {cell}, %dil",
                        f"\t call bf_print"])
        elif instruction.operator == "loop":
            last_label +=1
            l_entry = f".L{last_label}"
            last_label +=1
            l_out = f".L{last_label}"
            asm.extend([f"{l_entry}:", 
                        f"\t mov {cell}, %al",
                        f"\t mov $0, %bl", 
                        f"\t cmp %al, %bl",
                        f"\t je {l_out}"])
            body, label_offset = to_asm(instruction.body, last_label)
            asm.extend(body)
            asm.extend([f"\t jmp {l_entry}"])
            asm.extend([f"{l_out}:"])
            last_label = label_offset

        elif instruction.operator == "input":
            asm.extend([f"\t xor %al, %al",
                        f"\t call bf_read", 
                        f"\t mov %al, {cell}"])    

            # asm.extend([f"\t xor %dil, %dil",
            # f"\t mov {cell}, %dil",
            # f"\t call bf_print"])
    return asm, last_label









            


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

    if(options.verbosity):
        print(f"After translation to intermediate representation, the list of instructions is: {intermediate}, the data pointer will be changed by {current_offset}")
    
    asm, tmp = to_asm(intermediate)
    asm.extend([f"\tretq"]) 

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
        shell_command = f"gcc -o {assembly_name[:-2]} {assembly_name} bf_runtime.c"
        gcc_stat = os.system(shell_command)
        if not (os.WIFEXITED(gcc_stat) and os.WEXITSTATUS(gcc_stat) == 0):
            print(f'ERROR: gcc exited abnormally')

    if (not options.save_asm):
        cleanup = f"rm {assembly_name}"
        os.system(cleanup)

    # try:
    #     program.execute(BFMemory())
    # except BFExit:
    #    pass

# --------------------------------------------------------------------
if __name__ == '__main__':
    _main()