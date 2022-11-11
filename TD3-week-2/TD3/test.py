import os
from pathlib import Path
import sys


if __name__ == '__main__':
    regression = 'regression'
    examples = 'examples'
   # print("Running examples tests, including lab1/2\n")
   # for fn in Path(examples).rglob('*.bx'):
   #     print(fn)
   #     os.system(f"python3 bxcc.py {fn}")
   #     print("\n ======================\n")

    print("Running regression tests\n")
    for fn in Path(regression).rglob('*.bx'):
        print(fn)
        os.system(f"python3 bxcc.py {fn}")
        print("\n ======================\n")
