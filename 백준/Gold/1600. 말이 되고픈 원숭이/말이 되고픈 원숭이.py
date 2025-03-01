import sys
from collections import deque
inp = sys.stdin.readline

# k는 말처럼 이동할 수 있는 횟수 의미
k = int(inp().strip())
m, n = map(int, inp().strip().split())
arr = [list(map(int, inp().strip().split())) for _ in range(n)]

# visit 배열은 n, m 짜리가 몇개 있어야하는가? 초기값은?
# k개(k번 이동 가능 == 0~k개 == k+1개 있어야함)
visit = [[[-1]*m for _ in range(n)] for _ in range(k+1)]
# [k+1] [n] [m]
# 1, 1에서 출발 -> n-1, m-1로 간다
horse_directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = -1

# n-1, m-1까지 도달 == res하고 비교해서 갱신해줘야함.
# if 현재 queue에서 뺀 데이터가 res보다 크거나 같다면 버리기-> continue
dq = deque()
# 말 흉내 횟수, x, y, (cnt 빼기??)
dq.append((0, 0, 0))
for kk in range(k+1):
    visit[kk][0][0] = 0
while dq:
    horsecnt, x, y = dq.popleft()
    if (x, y) == (n-1, m-1):
        res = visit[horsecnt][x][y]
        print(res)
        exit(0)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1: continue
        # if visit[horsecnt][nx][ny] != -1 and visit[horsecnt][x][y]+1 > visit[horsecnt][nx][ny]: continue
            # 더 빠르게 가능 방법 찾은것. -> 추가하기 == 반대로는 >인 경우 continue
        if visit[horsecnt][nx][ny] == -1:
            dq.append((horsecnt, nx, ny))
            visit[horsecnt][nx][ny] = visit[horsecnt][x][y]+1
        # print(horsecnt, nx, ny, "말")

    if horsecnt+1 > k: continue # 말처럼 흉내 못냄
    for dx, dy in horse_directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1: continue 
        if visit[horsecnt + 1][nx][ny] == -1:  # 방문하지 않은 경우만
        # if visit[horsecnt+1][nx][ny] != -1 and visit[horsecnt][x][y]+1 > visit[horsecnt+1][nx][ny]: continue
    
            dq.append((horsecnt+1, nx, ny))
            visit[horsecnt+1][nx][ny] = visit[horsecnt][x][y]+1

print(res)