import sys
inp = sys.stdin.readline

t = int(inp())

for i in range(t):
    a,b = map(int, inp().split())
    print(a+b)