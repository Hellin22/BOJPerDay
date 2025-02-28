import sys
from collections import deque
inp = sys.stdin.readline

n, m, player_cnt = map(int, inp().strip().split())
player_make_castle = [0] + list(map(int, inp().strip().split()))
player_castle_cnt = [0] * (player_cnt+1)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

arr = [list(inp().strip()) for _ in range(n)]

dq_list = [0] + [deque() for _ in range(player_cnt)]
visit = [0] + [[[-1]*m for _ in range(n)] for _ in range(player_cnt)]

for i in range(n):
    for j in range(m):
        if arr[i][j] != '.' and arr[i][j] != '#':
            arr[i][j] = int(arr[i][j])
            dq_list[arr[i][j]].append((0, i, j))
            visit[arr[i][j]][i][j] = 0
            player_castle_cnt[arr[i][j]] +=1


def bfs(num, round): # dq[num] 번 deque에 대해서 bfs 진행. 얼마동안 진행?
    global n, m
    dq = dq_list[num]
    for i in range(len(dq_list[num])):
        cnt, x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] != '.': continue # 본인과 똑같은 값이라도 안가도됨
            if visit[num][nx][ny] != -1 and visit[num][nx][ny] <= 1: continue # 동일해도 visit 안해줘도 됨
            
            arr[nx][ny] = num
            visit[num][nx][ny] = 1
            dq.append((1, nx, ny))
            player_castle_cnt[num]+=1

    while dq: # dq에서 bfs 돌리다가 cnt가 player_make_castle[num]과 동일해지면 종료해야함.
        cnt, x, y = dq.popleft()
        if cnt == player_make_castle[num]:
            dq.append((cnt, x, y))
            return dq # 리턴한 dq를 다시 dq_list[num]에다가 추가(바꾸기)
        
        # 만약 cnt가 아니라면 1 현재 위치를 바꾸고 visit 갱신해주고 상황에 따라 추가
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] != '.': continue # 본인과 똑같은 값이라도 안가도됨
            if visit[num][nx][ny] != -1 and visit[num][nx][ny] <= cnt+1: continue # 동일해도 visit 안해줘도 됨
            
            arr[nx][ny] = num
            visit[num][nx][ny] = cnt+1
            dq.append((cnt+1, nx, ny))
            player_castle_cnt[num]+=1

    return None
cnt = 0
round = 0
while True:
    None_cnt = 0
    # print(*dq_list[1:])
    for i in range(1, player_cnt+1):
        if dq_list[i] is not None:
            dq_list[i] = bfs(i, round)
            # print(i, dq_list[i])
        if dq_list[i] is None: None_cnt+=1
    if None_cnt == player_cnt:
        print(*player_castle_cnt[1:])
        # print(round)
        # print(arr)
        exit()
    cnt+=1
    round+=1