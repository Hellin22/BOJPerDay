import sys
inp = sys.stdin.readline

n = int(inp().strip())
an = set(map(int, inp().split()))
m = int(inp().strip())
am = list(map(int, inp().split()))

for i in am:
    if(i in an):
        print(1)
    else:
        print(0)