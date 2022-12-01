#! /usr/bin/env python3


import sys

from brainfuck import BFExit, BFInstruction, BFMemory


def _main():
    if len(sys.argv)-1 != 1:
        print(f'Usage: {sys.argv[0]} [FILE.bf]', file = sys.stderr)
        exit(1)

    with open(sys.argv[1]) as stream:
        program = stream.read()
    program = BFInstruction.parse(program)

    print(program)

    try:
        program.execute(BFMemory())
    except BFExit:
        pass

# --------------------------------------------------------------------
if __name__ == '__main__':
    _main()