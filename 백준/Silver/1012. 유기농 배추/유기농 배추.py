import sys
from collections import deque

inp = sys.stdin.readline
t = int(inp().strip())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(m, n, arr, visit):
    q = deque()
    bug = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visit[i][j]:
                q.append([i, j])
                bug+=1
                while q:
                    curs = q.popleft()
                    for k in range(4):
                        nx, ny = curs[0] + dx[k], curs[1] + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] or arr[nx][ny] != 1: continue
                        visit[nx][ny] = True
                        q.append([nx, ny])
    return bug

def initt(m, n, k):
    arr = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    for i in range(k):
        y, x = map(int, inp().strip().split())
        arr[x][y] = 1
    return arr, visit
for _ in range(t):
    m, n, k = map(int, inp().strip().split())
    arr, visit = initt(m, n, k)
    print(bfs(m, n, arr, visit))

