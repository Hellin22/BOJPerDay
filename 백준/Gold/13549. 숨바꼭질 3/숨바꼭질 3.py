import sys
from collections import deque
inp = sys.stdin.readline

n, k = map(int, inp().strip().split())
visit = [100002] * 100001

dq = deque()
dq.append([n, 0])
visit[n] = 0
while dq:
    x, ttime = dq.popleft()
    if x == k: break
    if x-1 >= 0 and visit[x-1] > ttime+1:
        dq.append([x-1, ttime+1])
        visit[x-1] = ttime+1
    if x+1 <= 100000 and visit[x+1] > ttime+1:
        dq.append([x+1, ttime+1])
        visit[x+1] = ttime+1
    if 2*x <= 100000 and visit[2*x] > ttime:
        dq.append([2*x, ttime])
        visit[2*x] = ttime

print(visit[k])
