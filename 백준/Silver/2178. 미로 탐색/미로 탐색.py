import sys
from collections import deque

inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = [list(map(int, inp().strip())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque()
q.append([0, 0, 1])
visit[0][0] = True

def bfs():
    while q:
        curs = q.popleft()
        for i in range(4):
            nx, ny = curs[0] + dx[i], curs[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] or arr[nx][ny] == 0: continue
            if nx == n-1 and ny == m-1:
                return curs[2] + 1
            visit[nx][ny] = True
            q.append([nx, ny, curs[2] + 1])

print(bfs())