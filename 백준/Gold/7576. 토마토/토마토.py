import sys
from collections import deque

inp = sys.stdin.readline

m, n = map(int, inp().strip().split())
arr = [list(map(int, inp().strip().split())) for _ in range(n)]

notRipedTomatoCnt = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j, 0])
        elif arr[i][j] == 0: notRipedTomatoCnt+=1
if notRipedTomatoCnt == 0: 
    print(0)
    exit()

def bfs():
    global notRipedTomatoCnt
    while q:
        curs = q.popleft()
        for i in range(4):
            nx, ny = curs[0] + dx[i], curs[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] != 0: continue
            arr[nx][ny] = 1
            notRipedTomatoCnt-=1
            if notRipedTomatoCnt == 0:
                return curs[2] + 1
            q.append([nx, ny, curs[2]+1])

res = bfs()
print(-1 if res is None else res)