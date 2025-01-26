import sys
from collections import deque
inp = sys.stdin.readline
n, m = map(int, inp().strip().split())

arr = [[0] * (m+1) for _ in range(n+1)]
visit = [[[-1] * 2 for _ in range(m+1)] for _ in range(n+1)]  # 0: 벽을 부수지 않음, 1: 벽을 부순 상태
for i in range(1, n+1):
    strs = inp().strip()
    for j in range(len(strs)):
        arr[i][j+1] = int(strs[j])
dx, dy = [0, 1, 0, -1],[1, 0, -1, 0]
q = deque()
q.append([1, 1, 0]) # x, y, 벽 부쉇는지
visit[1][1][0] = 1
while q:
    curs = q.popleft()
    
    for i in range(4):
        nx, ny = curs[0] + dx[i], curs[1] + dy[i]
        if nx <= 0 or ny <= 0 or nx > n or ny > m: continue
        if nx == n and ny == m: 
            print(visit[curs[0]][curs[1]][curs[2]] + 1)
            exit()
        if arr[nx][ny] == 1 and curs[2] == 0:
            if visit[nx][ny][1] == -1:
                q.append([nx, ny, 1])
                visit[nx][ny][1] = visit[curs[0]][curs[1]][0] + 1
        elif arr[nx][ny] == 0 and visit[nx][ny][curs[2]] == -1:
            q.append([nx, ny, curs[2]])
            visit[nx][ny][curs[2]] = visit[curs[0]][curs[1]][curs[2]] + 1

if(n == 1 and m == 1): print(1)
else: print(-1)