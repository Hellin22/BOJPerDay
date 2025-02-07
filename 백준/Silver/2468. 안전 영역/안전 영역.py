import sys
from collections import deque
inp = sys.stdin.readline
n = int(inp())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
arr = [list(map(int, inp().split())) for _ in range(n)]
maxHeight = max(max(row) for row in arr)
res = 1
for height in range(1, maxHeight):
    visit = [[False] * n for _ in range(n)]
    q = deque()
    safeZone = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == True or arr[i][j] <= height: continue
            visit[i][j] = True
            q.append([i, j])
            safeZone+=1
            while q:
                curs = q.popleft()
                for k in range(4):
                    nx, ny = curs[0] + dx[k], curs[1] + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] == True or arr[nx][ny] <= height: continue
                    visit[nx][ny] = True
                    q.append([nx, ny])
    res = max(res, safeZone)

print(res)