import sys
from collections import deque

inp = sys.stdin.readline

m, n, h = map(int, inp().strip().split())

arr = []
for _ in range(h): 
    floor = [list(map(int, inp().strip().split())) for _ in range(n)]
    arr.append(floor)
visit = [[[False] * m for _ in range(n)] for _ in range(h)]

notTomato = 0
q = deque()

for i in range(n):
    for j in range(m):
        for k in range(h):
            if arr[k][i][j] == 0:
                notTomato+=1
            elif arr[k][i][j] == 1:
                q.append([i, j, k, 0])
                visit[k][i][j] = True

dx, dy, dz = [0, 1, 0, -1, 0, 0],[1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, -1]

def bfs(arr, visit, notTomato):
    if notTomato == 0: return 0
    while q:
        curs = q.popleft()
        for i in range(6):
            nx, ny, nz = curs[0] + dx[i], curs[1] + dy[i], curs[2] + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h or visit[nz][nx][ny] or arr[nz][nx][ny] != 0: continue
            notTomato -=1
            if notTomato == 0:
                return curs[3]+1
            q.append([nx, ny, nz, curs[3]+1])
            visit[nz][nx][ny] = True

res = bfs(arr, visit, notTomato)
print(-1 if res is None else res)
