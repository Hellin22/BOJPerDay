import sys
inp = sys.stdin.readline

a=int(inp())
b=0
for i in range(1, a+1):
    b+=i

print(b)
