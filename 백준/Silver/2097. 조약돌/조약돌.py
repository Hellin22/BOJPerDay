import sys
import math
inp = sys.stdin.readline

n = int(inp().strip())
k = int(math.ceil(math.sqrt(n)))

if n in (1, 2, 3, 4):
    res = 4 
elif n >= k*k-k+1:
    res = (k-1)*4
else:
    res = (k-1)*4-2

print(res)