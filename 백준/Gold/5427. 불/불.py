import sys
from collections import deque

inp = sys.stdin.readline

t = int(inp().strip())

def init():
    m, n = map(int, inp().strip().split())
    arr = [list(inp().strip()) for _ in range(n)]

    return n, m, arr

dx, dy = [0, 1, 0, -1],[1, 0, -1, 0]

def bfs(n, m, arr):
    q = deque()
    fire = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "@":
                peoplex, peopley = i, j
            elif arr[i][j] == "*":
                fire.append([i, j])

    q.append([peoplex, peopley, 0])
    for i in fire:
        q.append([i[0], i[1], 0])

    while q:
        curs = q.popleft()
        for i in range(4):
            nx, ny = curs[0] + dx[i], curs[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                if arr[curs[0]][curs[1]] == "@":
                    return curs[2]+1
                else: continue
            
            if arr[nx][ny] == "#": continue
            if arr[curs[0]][curs[1]] == "@":
                if arr[nx][ny] == ".": 
                    arr[nx][ny] = "@"
                    q.append([nx, ny, curs[2]+1])
            elif arr[curs[0]][curs[1]] == "*":
                if arr[nx][ny] == "@":
                    arr[nx][ny] = "*"
                if arr[nx][ny] == ".": 
                    arr[nx][ny] = "*"
                    q.append([nx, ny, curs[2]+1])

for _ in range(t):
    n, m, arr = init()
    res = bfs(n, m, arr)
    print("IMPOSSIBLE" if res is None else res)
