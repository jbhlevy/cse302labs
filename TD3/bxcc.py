"""
Going from .bx to x64 (currently stops at tac...)
"""
import json
import os
from pathlib import Path
from bx2ast import Reader
from ast2tac import Prog
import tac2x64 as x64
import sys 

def bx_to_tac(source_name):
    with open(source_name, 'r') as bx_file:
        source = bx_file.read()
    reader = Reader(source_name, source)
    ast_object = reader.read()
    #print(ast_object.block.stmts)
    prog = Prog(ast_object, 'tmm')
    js = prog.js_obj
    dest_name = str(source_name)[:-2] + 'tac.json'
    with open(dest_name, 'w') as dest_file:
        json.dump(js, dest_file)
    #print(f'{source_name} -> {dest_name}')
    return dest_name

# We use this function that takes as input a tac.json file and creates the .s file. 
# It then poceeds to 
def main():
    fn = sys.argv[1]
    #print(fn)
    tac_name = bx_to_tac(fn)
    s_name = x64.compile_tac_from_json(tac_name)
    name = s_name[:-2]
    #print(name, s_name)
    shell_command = f"gcc -o {name} {s_name} bx_runtime.c"
    #print(shell_command)
    gcc_stat = os.system(shell_command)
    if not (os.WIFEXITED(gcc_stat) and os.WEXITSTATUS(gcc_stat) == 0):
          print(f'gcc exited abnormally')
    print(f"{fn} -> {s_name} -> {name}")









def main1():
    """We perform the translation to asm for all the files in examples"""
    for fn in Path('examples').rglob('*.bx'): 
        #print(fn)
        tac_name = bx_to_tac(fn)
        s_name = x64.compile_tac_from_json(tac_name)
        name = s_name[:-2]
        shell_command = f"gcc -o {name} {s_name} bx_runtime.c"
        gcc_stat = os.system(shell_command)
        if not (os.WIFEXITED(gcc_stat) and os.WEXITSTATUS(gcc_stat) == 0):
          print(f'gcc exited abnormally')
        print(f"{fn} -> \n\t{s_name} \n\t\t-> {name}")

main1()