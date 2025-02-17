import sys
from collections import deque

inp = sys.stdin.readline

n, k = map(int, inp().strip().split())
if n == k:
    print(0)
    exit()
q = deque()
q.append([n, 0])
st = {n}
def bfs():
    global k
    while q:
        curs = q.popleft()
        for nx in (curs[0]-1, curs[0]+1, curs[0]*2):
            if nx == k: return curs[1]+1

            if 0 <= nx and  nx <= 100001 and nx not in st:
                q.append([nx, curs[1]+1])
                st.add(nx)
print(bfs())