import sys
inp = sys.stdin.readline

# 세로 r칸 가로 c칸 -> r*c # 65, 90
n, m = map(int, inp().strip().split(" "))
arr = [[0] * m for _ in range(n)]
alphabet = [0] * 26
dx, dy = [0, 1, 0, -1],[1, 0, -1, 0]
maxx = -1
visit = [[0] * m for _ in range(n)]

for i in range(n):
    strr = inp().strip()
    for j in range(m):
        arr[i][j] = ord(strr[j]) - 65

def dfs(x, y, cnt):
    global maxx
    maxx = max(maxx, cnt)
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1: continue
        if alphabet[arr[nx][ny]] == 1: continue
        alphabet[arr[nx][ny]] = 1
        visit[nx][ny] = 1
        dfs(nx, ny, cnt+1)
        visit[nx][ny] = 0
        alphabet[arr[nx][ny]] = 0

alphabet[arr[0][0]] = 1
visit[0][0] = 1
dfs(0, 0, 1)

print(maxx)