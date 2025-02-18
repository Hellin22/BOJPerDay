import sys
from collections import deque
inp = sys.stdin.readline

# nm은 2~6 -> bfs

n, m = map(int, inp().strip().split())
dx, dy = [1, 1, 1],[-1, 0, 1]

arr = [list(map(int, inp().strip().split())) for _ in range(n)]
min_arr = [[[601] * m for _ in range(n)] for _ in range(3)]
q = deque()

def bfs(n, m):
    for j in range(m):
        for k in range(3):
            min_arr[k][0][j] = arr[0][j]
            q.append([0, j, k, min_arr[k][0][j]]) # x, y, dir, val    
    while q:
        curs = q.popleft()
        # if min_arr[curs[0]][curs[1]] < curs[3]: continue # 방향이 있기 때문에 단지 숫자가 작다고 이렇게 하면 안됨.
        # min_arr에다가 min_arr[i][j][k] -> k는 0, 1, 2이 존재함. 즉, k는 크기가 3임.
        if min_arr[curs[2]][curs[0]][curs[1]] < curs[3]: continue
        for i in range(3):
            nx, ny = curs[0] + dx[i], curs[1]+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or curs[2] == i or min_arr[i][nx][ny] < curs[3] + arr[nx][ny]: continue
            min_arr[i][nx][ny] = curs[3] + arr[nx][ny]
            q.append([nx, ny, i, min_arr[i][nx][ny]])

    min_res = 701
    for k in range(3):
        for j in range(m):
            if min_arr[k][n-1][j] < min_res:
                min_res = min_arr[k][n-1][j]
    return min_res

print(bfs(n, m))