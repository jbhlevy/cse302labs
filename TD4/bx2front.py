"""
This file contains the implementation of the Reader class. 
The Reader is composed of a lexer and a parser (from the PLY library). 
It takes as input a source file (.bx) and generates the corresponding ast in json format (json can be dumped in a file)
"""
import json
import sys
from lex_pars import Lexer, Parser

"""
Part A of the file: Reader 
The Reader classe encapsulates the Lexer and the Parser. 
Thanks to this we only need to class the read(self) method in order to obtain the first node of the AST object. 
"""
# ================================================================================

class Reader:
    def __init__(self, source_name: str, data: str):
        self.lexer = Lexer(source_name, data)
        self.parser = Parser(self.lexer)

    def read(self):
        return self.parser.parse()

def main():
    with open(bx_filename, 'r') as bx_file:
        source = bx_file.read()
        source_name = bx_filename
        reader = Reader(source_name, source) # Creating the reader object
        ast_object = reader.read()
        if not ast_object:
            raise SyntaxError(f"Error while parsing")
        ast_object.type_check([]) 


if __name__ == "__main__":
    bx_filename = sys.argv[1]
    if not bx_filename.endswith('.bx'):
        print(f'File {bx_filename} does not have .bx extension')
        sys.exit(1)
    main()