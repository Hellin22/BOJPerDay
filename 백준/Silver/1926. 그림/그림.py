import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = [list(map(int, inp().split())) for _ in range(n)]

visit = [[0] * m for _ in range(n)]
q = deque()
dx, dy = [1, 0, -1, 0],[0, 1, 0, -1]
res = 0
max_ner = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visit[i][j] == 0:
            q.append([i, j])
            res += 1
            tmp_max = 1
            visit[i][j] = 1
            while q:
                curs = q.popleft()
                for k in range(4):
                    nx = curs[0] + dx[k]
                    ny = curs[1] + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1 or arr[nx][ny] == 0: continue
                    tmp_max+=1
                    q.append([nx, ny])
                    visit[nx][ny] = 1
            max_ner = max(max_ner, tmp_max)
print(res)
print(max_ner)