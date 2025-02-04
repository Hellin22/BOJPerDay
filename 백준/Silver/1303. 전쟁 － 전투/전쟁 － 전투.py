import sys
from collections import deque

inp = sys.stdin.readline

m, n = map(int, inp().strip().split())
arr = [list(inp().strip()) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
wNum, bNum = 0, 0
q = deque()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(n):
    for j in range(m):
        if visit[i][j] == 1: continue
        curColor = arr[i][j]
        visit[i][j] = 1
        q.append([i, j])
        curSize = 1
        while q:
            curs = q.popleft()
            for k in range(4):
                nx = curs[0] + dx[k]
                ny = curs[1] + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1 or curColor != arr[nx][ny]: continue
                curSize+=1
                visit[nx][ny] = 1
                q.append([nx, ny])
        if curColor == "W":
            wNum += curSize*curSize
        else: bNum += curSize*curSize
print(wNum, bNum)