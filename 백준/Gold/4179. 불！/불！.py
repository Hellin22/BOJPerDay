import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = [list(inp()) for _ in range(n)]

q = deque()

fire = []
jj = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == "J": 
            jj.append([i, j])
        elif arr[i][j] == "F":
            fire.append([i, j])
            
for i in range(len(fire)):
    q.append([fire[i][0], fire[i][1], 0])
q.append([jj[0][0], jj[0][1], 0])

# visit = [[0] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
while q:
    curs = q.popleft()
    for i in range(4):
        nx = curs[0] + dx[i]
        ny = curs[1] + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            if arr[curs[0]][curs[1]] == "J": 
                print(curs[2]+1)
                exit()
            else:
                continue
        if arr[curs[0]][curs[1]] == "F": # 불
            if arr[nx][ny] == ".":
                arr[nx][ny] = "F"
                q.append([nx, ny, curs[2]+1])
        elif arr[curs[0]][curs[1]] == "J": #사람
            if arr[nx][ny] == ".":
                arr[nx][ny] = "J"
                q.append([nx, ny, curs[2]+1])

print("IMPOSSIBLE")