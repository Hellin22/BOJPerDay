import sys
from collections import deque
inp = sys.stdin.readline

n, m, k = map(int, inp().strip().split())
arr = [list(inp().strip()) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북

curx, cury, goalx, goaly = map(int, inp().strip().split())
curx, cury = curx-1, cury-1
res = 0

q = deque()
q.append([curx, cury])
visit[curx][cury] = 0

def bfs():
    while q:
        x, y= q.popleft()
        for i in range(4):
            for j in range(1, k+1):
                nx, ny = x + dx[i] * j, y + dy[i]*j
                if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == "#": break
                if (visit[nx][ny] != -1 and visit[nx][ny] == visit[x][y]+1): continue
                if (visit[nx][ny] != -1 and visit[nx][ny] < visit[x][y]+1): break
                
                # 한번도 안갔거나 or 갈 곳의 가중치가 더 큰경우 업데이트
                q.append([nx, ny])
                visit[nx][ny] = visit[x][y]+1
                if nx == goalx-1 and ny == goaly-1: 
                    print(visit[nx][ny])
                    exit()
bfs()

print(visit[goalx-1][goaly-1])