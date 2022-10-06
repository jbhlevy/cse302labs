"""
This file contains the implementation of the Reader class. 
The Reader is composed of a lexer and a parser. 
It takes as input a source file (.bx) and generates the corresponding ast in json format (json can be dumped in a file)
"""
from asyncore import read
from lex_pars import Lexer, Parser

class Reader:
    def __init__(self, source_name, data):
        self.lexer = Lexer(source_name, data)
        self.parser = Parser(self.lexer)

    def read(self):
        return self.parser.parse()

# =========== Driver Code to test only the reader =======
if __name__ == '__main__':
    import sys
    import json

    def write_out(source_name, source, ast_obj):
        dest_name = source_name[:-2] + 'json'
        js = {
            "provenance": source_name, 
            "source": source,
            "ast": ast_obj.prog_to_json
    }


        with open(dest_name, 'w') as dest_file:
            json.dump(js, dest_file)
        print(source_name + '->' + dest_name)

    source_name = sys.argv[1]
    assert source_name.endswith('.bx')
    with open(source_name, 'r') as bx_file:
        source = bx_file.read()
    reader = Reader(source_name, source)
    ast_obj = reader.read()
    print(ast_obj)
    write_out(source_name, source, ast_obj)
