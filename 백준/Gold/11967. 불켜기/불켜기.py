import sys
from collections import deque

inp = sys.stdin.readline

n, m = map(int, inp().strip().split())
switch_llist = dict()
for i in range(m):
    a, b, c, d = map(int, inp().strip().split())
    if (a-1, b-1) in switch_llist:
        switch_llist[(a-1, b-1)] = switch_llist[(a-1, b-1)] + (c-1, d-1)
    else:
        switch_llist[(a-1, b-1)] = (c-1, d-1)

# 1. (1, 1)에서 시작함
# 2. x, y에서 스위치 켤 수 있는 모든곳의 좌표에 대해 불켜기 진행(arr[a][b] = 1 == 불켜기) 
# 3. 만약 불을 못켬 + 이미 켰음 == 상하좌우를 보고 큐에 append
# 4. -> 여까지 보면 q에서 뺄 때 스위치 on + 그거에 대해서 진행
# 5. 불을 킬 수 있음 -> 그 좌표를 bfs q의 가장 앞에(append left) 추가하기!!
# 5.1. 아닌니니니 만약 5번의 좌표에 대해서 상하좌우 visit이 1인게 하나라도 있으면 추가하기 
# 5.2. 만약에 상하좌우 1인게 0개이다. -> 그러면 불켜진 상태지만 못가는거니까 가만히 놔두기 
# 6. 큐가 빌때까지 진행하기
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
arr = [[0] * n for _ in range(n)] # 0이면 불x, 1이면 불o
visit = [[False] * n for _ in range(n)] # False이면 방문x, True이면 방문o
res = 0 # 불켜진곳 cnt
dq = deque()

arr[0][0] = 1 # 불켜짐 -> 원래 켜져있었음
res+=1
dq.append((0, 0))
visit[0][0] = True # 방문처리

while dq:
    x, y = dq.popleft()
    if (x, y) in switch_llist:
        sett = switch_llist[(x, y)]
        for i in range(0, len(sett), 2):
            x1, y1 = sett[i], sett[i+1]
            if arr[x1][y1] == 0: # 불 안켜진 상태
                arr[x1][y1] = 1 # 불 켜주기
                res+=1
                for dx, dy in directions:
                    nx, ny = x1 + dx, y1 + dy
                    if 0<=nx< n and 0<=ny <n and visit[nx][ny] is True: # 방문한 곳이 사방에 하나라도 있다면
                        dq.appendleft((x1, y1))
                        visit[x1][y1] = True # 방문표시(방문 가능하기 때문)
                        break
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0<=nx< n and 0<=ny <n and arr[nx][ny] == 1 and visit[nx][ny] is False: 
            # 불이 켜져있는데 방문을 안한곳이 있다면 그곳으로 가야함.
            dq.append((nx, ny))
            visit[nx][ny] = True

print(res)

