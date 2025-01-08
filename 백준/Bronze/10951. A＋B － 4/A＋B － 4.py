import sys

for line in sys.stdin:
    if line.strip():
        a, b = map(int, line.split())
        print(a+b)