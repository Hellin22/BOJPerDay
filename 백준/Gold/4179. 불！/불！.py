import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = [list(inp()) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque()
fire = []
jx, jy = 0, 0

def assignn():
    for i in range(n):
        global jx, jy
        for j in range(m):
            if arr[i][j] == "J":
                jx, jy = i, j
            elif arr[i][j] == "F":
                fire.append([i, j])
def qadd():
    for i in range(len(fire)):
        q.append([fire[i][0], fire[i][1], 0])
    q.append([jx, jy, 0])
def bfs():
    while q:
        curs = q.popleft()
        for i in range(4):
            nx = curs[0] + dx[i]
            ny = curs[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                if arr[curs[0]][curs[1]] == "J": 
                    return curs[2]+1
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
assignn()
qadd()
res = bfs()
print("IMPOSSIBLE" if res == None else res)