import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())
arr = [[0] * (n+1) for _ in range(n+1)]
appleCnt = int(inp())
for i in range(appleCnt):
    x, y = map(int, inp().strip().split())
    arr[x][y] = 9

L = int(inp())
curTime = 0
dir = 0
dx, dy = [0, 1, 0 ,-1], [1, 0, -1, 0]
snakeChangeDirection = deque()
for i in range(L):
    cd = list(inp().strip().split())
    cd[0] = int(cd[0])
    snakeChangeDirection.append(cd)
q = deque()
snake = []
q.append([1, 1])
arr[1][1] = 1
curHead = [1, 1]
while q:
    nx, ny = curHead[0]+dx[dir], curHead[1]+dy[dir]

    if nx <= 0 or ny <= 0 or nx > n or ny > n or arr[nx][ny] == 1: 
        curTime+=1
        break
    q.append([nx, ny])
    curHead = [nx, ny]
    if arr[nx][ny] != 9:
        curs = q.popleft()
        arr[curs[0]][curs[1]] = 0
    arr[nx][ny] = 1

    curTime+=1
    if not snakeChangeDirection or snakeChangeDirection[0][0] != curTime: continue
    if snakeChangeDirection[0][1] == "D": # 오른쪽 90도 회전
        dir = (dir+1)%4
    else: # 왼쪽 90도 회전
        dir = (dir-1)%4
    snakeChangeDirection.popleft()

print(curTime)
