import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp().strip())
sharkx, sharky, curLevel, curEat = 0, 0, 2, 0
arr = [[0] * n for _ in range(n)] # 0~n-1
res = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] # 북서남동 (우선순위에 따라서)
for i in range(0, n):
    oneRow = list(map(int, inp().strip().split(" ")))
    for j in range(0, n):
        arr[i][j] = oneRow[j]
        if(arr[i][j] == 9): 
            sharkx, sharky = i, j

q = deque()
# canEatList = [] # eatx, eaty를 해놓으면 이거 필요없을듯?

while True:
    visit = [[0] * n for _ in range(n)]
    visit[sharkx][sharky] = 1
    # 좌표 정해놔야지...
    # 그러면 거리, 좌표 2개, flag 이렇게 총 4개를 저장해놔야하네 ㅋㅋ
    anyFlag = False # true로 바뀌면 큐에 더이상 추가 x
    eatx, eaty = -1, -1
    distance = -1
    q.append([sharkx, sharky, 0])

    while(len(q) != 0):
        cur = q.popleft()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] == 1 or arr[nx][ny] > curLevel: continue        
            # 상어가 먹을 수 있다면? -> 일단 물고기가 존재해야함. == arr[nx][ny] != 0
            if arr[nx][ny] < curLevel and arr[nx][ny] != 0:
                visit[nx][ny] = 1
                if anyFlag == False: # 먹을수 있는 최초의 물고기임 -> eatxy 설정하기
                    anyFlag = True
                    eatx, eaty = nx, ny
                    distance = cur[2] + 1

                else: # 이미 먹는게 갱신됐다면 -> distance비교 -> eatxy 비교하기
                    if cur[2] + 1 != distance: continue # 거리가 다르다면(더 멀면) 안함.
                    # 가장 위쪽 + 가장 왼쪽
                    if eatx < nx: continue # eatx가 더 위쪽이면 그대로
                    elif eatx == nx: # x가 똑같으면 y 비교하기
                        if eaty < ny: # eaty가 더 왼쪽이니 그대로
                            continue
                        else: # nx, ny로 교체
                            eatx, eaty = nx, ny
                    else: # eatx > nx -> 바로 교체하기
                        eatx, eaty = nx, ny
            elif arr[nx][ny] == 0 or arr[nx][ny] == curLevel: # 벽인 경우 -> 큐에 넣기
                if anyFlag == True: continue
                else: 
                    visit[nx][ny] = 1
                    q.append([nx, ny, cur[2]+1])


    # bfs 종료임 -> eatx, eaty 보기 -> eatx가 -1이다 == print(res)
    if eatx == -1:
        print(res)
        exit()

    res += distance
    arr[sharkx][sharky] = 0
    sharkx, sharky = eatx, eaty
    arr[sharkx][sharky] = 9
    curEat += 1
    if curLevel == curEat:
        curLevel+=1
        curEat=0
