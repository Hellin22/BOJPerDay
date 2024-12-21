import sys
inp = sys.stdin.readline

sett = set()

for i in range(10):
    a = int(inp().strip())
    sett.add(a%42)

print(len(sett))