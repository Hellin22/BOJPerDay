# 모든 나라에는 인구가 존재.
# 나라간의 인구 차이가 L ~ R 사이라면 국경 공유 가능 -> 국경 공유해서 인구가 이동
# 더이상 인구 이동이 없을때까지 이동해야함.
import sys, math
from collections import deque
inp = sys.stdin.readline

n, L, R = map(int, inp().strip().split())
arr = [list(map(int, inp().strip().split())) for _ in range(n)]
cnt = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
flag = False

def startt():
    global arr, cnt, flag
    while True:
        visit = [[0] * n for _ in range(n)]
        flag = False
        for i in range(n):
            for j in range(n):
                if visit[i][j] == 1: continue
                bfs(i, j, visit)
        if flag == False: 
            return
        cnt+=1

def bfs(x, y, visit):
    global flag
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    allPeopleCnt = arr[x][y]
    allXY = [[x, y]]
    while q:
        curs = q.popleft()

        for i in range(4):
            nx = curs[0] + dx[i]
            ny = curs[1] + dy[i]
            if(nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] == 1 
            or abs(arr[curs[0]][curs[1]] - arr[nx][ny]) > R or abs(arr[curs[0]][curs[1]] - arr[nx][ny]) < L): continue

            flag = True
            allXY.append([nx, ny])
            allPeopleCnt+=arr[nx][ny]
            q.append([nx, ny])
            visit[nx][ny] = 1
    
    peopleCnt = allPeopleCnt//len(allXY)
    for i in range(len(allXY)):
        arr[allXY[i][0]][allXY[i][1]] = peopleCnt

startt()
print(cnt)