import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().strip().split(" "))
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
arr = []
arr2 = []
res = -1

viruses = []
canWalls = []

def newWall(idx, cnt):
    if cnt == 3: 
        bfs()
        return

    for i in range(idx, len(canWalls)):
        cur = canWalls[i]
        arr[cur[0]][cur[1]] = 1
        newWall(i+1, cnt+1)
        arr[cur[0]][cur[1]] = 0

def bfs():
    global res
    arr2 = [row[:] for row in arr] # 배열 복사
    visit = [[0] * m for _ in range(n)]

    safeCnt = len(canWalls)-3
    q = deque()
    for i in range(len(viruses)):
        q.append([viruses[i][0], viruses[i][1]])

    while len(q) != 0:
        curs = q.popleft() # x, y
        # 0이면 집어넣기기
        for i in range(4):
            nx = curs[0] + dx[i]
            ny = curs[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr2[nx][ny] == 2 or arr2[nx][ny] == 1 or visit[nx][ny] == 1: continue
            q.append([nx, ny])
            arr2[nx][ny] = 2
            visit[nx][ny] = 1
            safeCnt-=1
    res = max(res, safeCnt)

for i in range(n):
    arr.append(list(map(int, inp().split(" "))))
    for j in range(len(arr[i])):
        if arr[i][j] == 2:
            viruses.append([i, j])
        if arr[i][j] == 0:
            canWalls.append([i, j])

newWall(0, 0)
print(res)