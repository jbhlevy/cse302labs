import json
import sys
from bx2front import Reader
import new_ast2tac


def main():
    with open(bx_filename, 'r') as bx_file:
        source = bx_file.read()
    source_name = bx_filename
    reader = Reader(source_name, source) # Creating the reader object
    ast_object = reader.read()
    if not ast_object:
        raise SyntaxError(f"Error while parsing")
    ast_object.type_check([])

    #Creating TAC
    tac_prog = new_ast2tac.Prog(ast_object, "tmm")
    js = tac_prog.js_obj
    dest_name = str(source_name)[:-2] + 'tac.json'
    with open(dest_name, 'w') as dest_file:
        json.dump(js, dest_file)
    return 1



if __name__ == "__main__":
    bx_filename = sys.argv[1]
    if not bx_filename.endswith('.bx'):
        print(f'File {bx_filename} does not have .bx extension')
        sys.exit(1)
    main()