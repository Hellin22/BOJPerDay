import sys
from collections import deque
inp = sys.stdin.readline

# 빙산이 2덩어리 이상으로 분리되는 최초의 시간
# 결국 visit 배열이 계쏙해서 새로 갱신되어야하나?
# 빙산의 위치만 visit하면 됨. n, m 모두 돌 필요가 없음.
# visit 배열은 새롭게 하는게 아니라
# visit 배열 다 돌고 나서는 현재 얼음 좌표들만 visit을 다시 0으로 바꿔주면 될듯
# -> 이 visit 배열을 도는것은 얼음이 들어있는 set만 돌면 됨.
# 얼음이 얼마나 녹을지를 결정해야함.
# 이거를 저장할 곳이 있으면 좋은데 말이지
# 그냥 이거도 set으로 할까?
# 1. visit 배열, 2. 빙산 arr, 3. 얼음 저장할 set, 3. 얼음 녹는거 저장할 set

n, m = map(int, inp().strip().split())
ice = [list(map(int,inp().strip().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
ice_coor = set()
will_be_melt_ice = set()
res = 0

for i in range(n):
    for j in range(m):
        if ice[i][j] != 0:
            ice_coor.add((i, j))
        else: visit[i][j] = 1 # 0은 방문 안해줘도 되기 때문임

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def melt():
    for ice_c in ice_coor:
        melt_cnt = 0
        for dx, dy in directions:
            nx, ny = ice_c[0] + dx, ice_c[1]+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if ice[nx][ny] == 0:
                melt_cnt+=1
        will_be_melt_ice.add((ice_c[0], ice_c[1], melt_cnt))
        # print(ice_c[0], ice_c[1], melt_cnt)

def melt_doing():
    ice_coor.clear()
    for melt_ice in will_be_melt_ice:
        # print(melt_ice)
        ice[melt_ice[0]][melt_ice[1]] = max(0, ice[melt_ice[0]][melt_ice[1]]-melt_ice[2])
        if ice[melt_ice[0]][melt_ice[1]] != 0:
            ice_coor.add((melt_ice[0], melt_ice[1]))
    will_be_melt_ice.clear()

def bfs():
    # ice_coor에 대해서 bfs 진행
    cnt = 0
    dq = deque()
    for x, y in ice_coor:
        if visit[x][y] == 0:
            dq.append((x, y))
            cnt+=1
        while dq:
            stx, sty = dq.popleft()
            for dx, dy in directions:
                nx, ny = stx + dx, sty + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1: continue
                visit[nx][ny] = 1
                dq.append((nx, ny))

    return cnt

def notvisit():
    for x, y in ice_coor:
        visit[x][y] = 0

res = 0
while True:
    # print()

    # for i in ice:
    #     print(*i)
    # print()

    ice_bfs = bfs()
    if ice_bfs == 0:
        print(0)
        exit()
    elif ice_bfs >= 2:
        print(res)
        exit()
    melt()
    melt_doing()
    notvisit()
    res+=1