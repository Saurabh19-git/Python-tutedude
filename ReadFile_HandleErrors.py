from pathlib import Path

fn = Path("sample.txt")

if fn.is_file():
    print("Reading file content:")
    with fn.open('rt') as fp:
        print(f"Line1:{fp.readline().rstrip()}")
        print(f"Line2:{fp.readline().rstrip()}")
else:
    print(f"The file '{fn.name}' was not found.")