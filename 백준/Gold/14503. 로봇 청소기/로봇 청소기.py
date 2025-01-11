import sys
import copy
from collections import deque # 큐를 위한 덱 선언

inp = sys.stdin.readline

# n, m이 주어짐 3~50
# 현재위치 r,c 로봇의 현재 dir이 주어짐 북동남서 0 1 2 3
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# +2 %4 해주기 -> 후진

# 왼쪽위가 00 (북서) 남동(n-1, m-1)
# r, c는 북쪽에서 r+1, 서쪽에서 c+1칸
# 1. 현재칸 청소
# 2. 주변 4칸중 청소x칸이 없으면 
#   1. 방향 유지한채로 한칸 후진 후 처음 1번
#   2. 후진 불가능(벽) -> 종료
# 3. 청소x칸 있으면
#   1. 반시계 회전
#   2. 방향 한칸 앞이 청소x면 한칸 전진
#   3. 처음 1번으로 돌아감
n, m = map(int, inp().strip().split()) # 행, 열
x, y, dir = map(int, inp().strip().split()) # 현재 좌표, 방향
arr = [list(map(int, inp().strip().split())) for _ in range(n)] # n줄에 걸쳐서 한줄 입력
visit = [[0] * m for _ in range(n)]
res = 0
q = deque()

# 현재 위치 청소 후 찾기 -> 청소기는 항상 빈칸에 오기 때문
# -> 청소가 된곳으로는 후진 가능하지만 벽으로는 후진을 못함
# 1. 큐가 필요한가? 안필요한거같네

while True: # 후진 못하면 종료해야함.
    # 1. 현재칸 청소
    # if(visit[x][y] == 1) # 근데 생각해보니까 무조건 뒤에서 종료 조건 있을거같네
    # while문 하나로 처리하려면 위 조건 필요
    if visit[x][y] == 0:
        visit[x][y] = 1
        res+=1
    canClean = False
    ndir = dir
    # 2. 청소할 수 있는 칸이 있다면 (반시계로 회전한겨)
    for _ in range(4):
        ndir = (ndir + 3) % 4
        nx = x + dx[ndir]
        ny = y + dy[ndir]
        if(nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1 or arr[nx][ny] == 1): continue
        # 이제 청소 가능한칸이 있는거임
        dir, x, y = ndir, nx, ny
        canClean = True
        break
    if canClean: # 청소 가능하냐?
        # 반시계로 회전했고 거기 갈 수 있따는 거니까 걸로 가면됨.
        # x, y, dir은 갱신완료 -> 이미 갱신된것.
        continue

    else: # 청소 가능한 칸이 없구나?
        # 후진 한방 갈기기
        nx = x + dx[(dir+2) % 4]
        ny = y + dy[(dir+2) % 4]

        if(nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1): break
        else: x, y = nx, ny 

print(res)