from pathlib import Path
from bx2ast import main as test


def testing_examples():
    print("Test starting...")
    for file in Path('../examples').rglob('*.bx'):
        print(f"\nTesting file: {file}")
        test(str(file))
    print("\nTest was sucessful, files can be found in directory json")
        
testing_examples()