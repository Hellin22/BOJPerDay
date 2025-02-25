import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp().strip())
arr = [list(map(int, inp().strip().split())) for _ in range(n)]
res = 10000
cur = 1
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and visit[i][j] == 0:
            arr[i][j] = cur
            
            q = deque()
            q.append((i, j))
            visit[i][j] = 1
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] == 1 or arr[nx][ny] == 0: continue
                    arr[nx][ny] = cur
                    q.append((nx, ny))
                    visit[nx][ny] = 1
            cur+=1

def bfs(x, y, num):
    global res
    visit = [[0]*n for _ in range(n)]
    bfs_q = deque()
    bfs_q.append((x, y, 0))
    visit[x][y] = 1
    while bfs_q:
        popx, popy, cnt = bfs_q.popleft()
        for dx, dy in directions:
            nx, ny = popx+dx, popy+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] == num or visit[nx][ny] == 1: continue
            # 종료 -> 처음으로 다른 지역 만나는 순간
            if arr[nx][ny] != 0:
                res = min(res, cnt+1)
                return
            
            bfs_q.append((nx, ny, cnt+1))
            visit[nx][ny] = 1


for i in range(n):
    for j in range(n):
        # 만약 처음 bfs시에 사방이 0이 아님 -> bfs 하지말기
        if arr[i][j] != 0: # arr[i][j]의 값도 파라미터로 보내주기
            flag = False
            for dx, dy in directions:
                nx, ny = x+dx, y+dy 
                if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] == arr[i][j]: continue
                flag = True
                break
            if flag: bfs(i, j, arr[i][j])

print(res-1)