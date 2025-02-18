import sys
from collections import deque
inp = sys.stdin.readline

dx, dy, dz = [0, 1, 0, -1, 0, 0],[1, 0, -1, 0, 0, 0],[0, 0, 0, 0, 1, -1]

while True:
    l, n, m = map(int, inp().strip().split())
    if (l, n, m) == (0, 0, 0): break
    arr = []
    for k in range(l):
        floor = []
        for i in range(n):
            strr = list(inp().strip())
            floor.append(strr)
        arr.append(floor)
        inp().strip()
    sx, sy, sz, ex, ey, ez = 0, 0, 0, 0, 0, 0
    for k in range(l):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == "S":
                    sz, sx, sy = k, i, j
                if arr[k][i][j] == "E":
                    ez, ex, ey = k, i, j
    
    q = deque()
    q.append([sz, sx, sy])
    arr[sz][sx][sy] = 0
    flag = False
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]
            if nz < 0 or nx < 0 or ny < 0 or nz >= l or nx >= n or ny >= m: continue
            if arr[nz][nx][ny] == "E": 
                print(f"Escaped in {arr[z][x][y]+1} minute(s).")
                q.clear()
                flag=True
                break
            if arr[nz][nx][ny] != ".": continue

            arr[nz][nx][ny] = arr[z][x][y]+1
            q.append([nz, nx, ny])
    if not flag:
        print("Trapped!")