from collections import deque
import sys
inp = sys.stdin.readline

n,m = map(int, inp().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    row = inp().strip()
    for j in range(len(row)):
        arr[i][j] = int(row[j])

q = deque()

# 1,1부터 시작
q.append((0, 0))

while q:
    curx, cury = q.popleft()
    for i in range(4):
        nx, ny = curx + dx[i], cury+dy[i]

        if(nx >= n or ny >= m or nx < 0 or ny < 0 or arr[nx][ny] == 0): continue
        if(arr[nx][ny] == 1):
            q.append((nx, ny))
            arr[nx][ny] = arr[curx][cury]+1

print(arr[n-1][m-1])