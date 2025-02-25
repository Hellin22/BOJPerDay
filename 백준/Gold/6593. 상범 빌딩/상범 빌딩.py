import sys
from collections import deque
inp = sys.stdin.readline
directions = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]# dz, dx, dy
# 4*5 -> 3번

def bfs(s_z, s_x, s_y):
    global n, m, h
    visit = [[[0] * m for _ in range(n)] for _ in range(h)]
    dq = deque()
    dq.append((s_z, s_x, s_y, 0))
    visit[s_z][s_x][s_y] = 1
    while dq:
        z, x, y, cnt = dq.popleft()
        for dz, dx, dy in directions:
            nz, nx, ny = z + dz, x+dx, y+dy
            if nz < 0 or nx < 0 or ny < 0 or nz >= h or nx >=n or ny >= m or visit[nz][nx][ny] == 1 or arr[nz][nx][ny] == "#": continue
            if arr[nz][nx][ny] == "E":
                return cnt+1
            visit[nz][nx][ny] = 1
            dq.append((nz, nx, ny, cnt+1))


while True:
    h, n, m = map(int, inp().strip().split())
    if (h, n, m) == (0, 0, 0): break
    arr = []
    s_x, s_y, s_z = 0, 0, 0
    # e_x, e_y, e_z = 0, 0, 0
    flag = False
    for height in range(h):
        sttr = []
        for x in range(n):
            sttr.append(inp().strip())
            if not flag:
                for y in range(m):
                    if sttr[x][y] == "S":
                        s_z, s_x, s_y = height, x, y
                        flag = True
                        break
        arr.append(sttr)
        inp()
    res = bfs(s_z, s_x, s_y)
    print("Trapped!" if res is None else f"Escaped in {res} minute(s).")
