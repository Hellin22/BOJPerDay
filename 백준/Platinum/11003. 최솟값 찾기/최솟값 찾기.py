import sys
from collections import deque
inp = sys.stdin.readline

n, l = map(int, inp().strip().split())
llist = list(map(int, inp().strip().split()))

dq = deque()
min_list = []
for i in range(len(llist)):
    while dq:
        if dq[0][1]+l <= i: 
            dq.popleft()
            continue
        if dq[-1][0] >= llist[i]: 
            dq.pop()
        elif dq[-1][0] < llist[i]: break 
    dq.append((llist[i], i))
    min_list.append(dq[0][0])

print(*min_list)