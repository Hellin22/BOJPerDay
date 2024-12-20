import sys
inp = sys.stdin.readline

n = int(inp())
str = "int"

for i in range(n//4):
    str=f"long {str}"

print(str)