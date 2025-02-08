import sys
from collections import deque
inp = sys.stdin.readline

tc = int(inp())
dx, dy = [-2, -1, 1, 2, 2, 1, -1, -2],[1, 2, 2, 1, -1, -2, -2, -1]
def bfs(curx, cury, targetx, targety, visit):
    res = 0
    q = deque()
    q.append([curx, cury, 0])
    visit[curx][cury] = True
    while q:
        curs = q.popleft()
        if curs[0] == targetx and curs[1] == targety: 
            res = curs[2]
            break
        for i in range(8):
            nx, ny = dx[i] + curs[0], dy[i] + curs[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny]: continue
            visit[nx][ny] = True
            q.append([nx, ny, curs[2]+1])

    return res

for case in range(tc):
    n = int(inp())
    res = 0
    curx, cury = map(int, inp().split())
    targetx, targety = map(int, inp().split())
    visit = [[False] * n for _ in range(n)]

    print(bfs(curx, cury, targetx, targety, visit))