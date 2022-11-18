import json
import sys
import tac2x64


def main():
    with open(tac_filename, 'r') as tac_file:
        js_obj = json.load(tac_file)
    asm = tac2x64.compile_tac(js_obj)



    #Creating TAC
    dest_name = str(tac_filename)[:-8] + 's'
    with open(dest_name, 'w') as dest_file:
        print(*asm, file=dest_file, sep='\n')
    return 1



if __name__ == "__main__":
    tac_filename = sys.argv[1]
    if not tac_filename.endswith('.tac.json'):
        print(f'File {tac_filename} does not have .tac.json extension')
        sys.exit(1)
    main()