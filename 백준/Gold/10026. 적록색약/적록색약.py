import sys
from collections import deque

inp = sys.stdin.readline
n = int(inp().strip())

arr = [list(inp().strip()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == "R":
            arr[i][j] = 0
        elif arr[i][j] == "G":
            arr[i][j] = 1
        else:
            arr[i][j] = 2

RGeqArr = [[0 if x == 1 else x for x in row] for row in arr]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(n, arr):
    visit = [[False] * n for _ in range(n)]
    q = deque()
    res = 0

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:  
                res += 1
                q.append((i, j))
                visit[i][j] = True
                color = arr[i][j]

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and arr[nx][ny] == color:
                            visit[nx][ny] = True
                            q.append((nx, ny))
    
    return res

print(bfs(n, arr), bfs(n, RGeqArr))
