import sys
import math

inp = sys.stdin.readline
n = int(inp().strip())
llist = list(map(int, inp().strip().split()))
if(len(llist) == 1):
    print(llist[0])
    exit()
res = llist[-1]
for i in range(len(llist)-2, -1, -1):
    if(llist[i] >= res):
        res = llist[i]
    else: # llist[i] < res
        res = llist[i] * math.ceil(res / llist[i])

print(res)