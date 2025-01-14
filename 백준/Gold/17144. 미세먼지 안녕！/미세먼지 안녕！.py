import sys
import math
inp = sys.stdin.readline

# r,c 1부터 시작
# -1은 공기청정기의 위치 (항상 1번열 + 무조건 존재 가능 -> 2개의 좌표 저장해놓기)
# 1. 미세먼지가 확산됨(/5 버림) -> 동시에 발생
# 2. 공기청정기 가동

n, m, t = map(int, inp().strip().split())
fresh = [] # fresh[0]는 공기청정기 윗부분, fresh[1]은 공기청정기 아래부분
res = 0 # 남아있는 먼지의 양
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
arr = [[0] * (m+1) for _ in range(n+1)]
arr2 = [[0] * (m+1) for _ in range(n+1)]
curMode = 1
for i in range(1, n+1):
    llist = list(map(int, inp().strip().split()))
    for j in range(0, m):
        arr[i][j+1] = llist[j]
        if arr[i][j+1] == -1: # 공기청정기 위치
            fresh.append(i) # 공기청정기는 항상 1번열

def zeroReset():
    for i in range(1, n+1):
        for j in range(1, m+1):
            arr2[i][j] = 0

    arr2[fresh[0]][1] = -1
    arr2[fresh[1]][1] = -1

def allPlace():
    for i in range(1, n+1):
        for j in range(1, m+1):
            spread(i, j)

def spread(x, y):
    # x, y에 대해서 spread 해야함.
    # 0이 아니라면 나눠서 willSpread에 저장해주기 (x, y, 미세먼지 값들)
    # 0이라면 continue
    # 아니라면 arr[x][y]에서 /5하고 floor한 값을 적용해야함.
    if arr[x][y] == 0 or arr[x][y] == -1: return
    minusNumber = math.floor(arr[x][y] / 5)
    ori = arr[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= 0 or ny <= 0 or nx >= n+1 or ny >= m+1 or (ny == 1 and (nx == fresh[0] or nx == fresh[1])): continue
        arr2[nx][ny] += minusNumber
        ori-=minusNumber
    arr2[x][y] += ori

def reverseClock():
    # 1. 1번 열
    for i in range(fresh[0]-1, 1, -1):
        arr2[i][1] = arr2[i-1][1]
    # 2. 1번 행
    for j in range(1, m, 1): # 8번 열은 3번에서 처리
        arr2[1][j] = arr2[1][j+1]
    # 3. m번 열
    for i in range(1, fresh[0], 1):
        arr2[i][m] = arr2[i+1][m]
    # 4.fresh[0]번 행
    for j in range(m, 2, -1): # 8은 7 ~ 3은 2 + 2번열은 0이 되어야함.
        arr2[fresh[0]][j] = arr2[fresh[0]][j-1]
    arr2[fresh[0]][2] = 0

def clock():
    # 1. 1번 열 arr[5][1] = arr[6][1]
    for i in range(fresh[1]+1, n, 1):
        arr2[i][1] = arr2[i+1][1]
    # 2. n번 행 arr[n][1] = arr[n][2] ~ arr[n][7] = arr[n][8]
    for j in range(1, m, 1):
        arr2[n][j] = arr2[n][j+1]
    # 3. m번 열 arr[7][8] = arr[6][8] ~ arr[fresh[1]+1][8] = arr[aresh[1]][8]
    for i in range(n, fresh[1], -1):
        arr2[i][m] = arr2[i-1][m]
    # 4. fresh[1]번 행 arr[fresh[1]][m] = arr[fresh[1]][m-1] ~ arr[][3] = arr[][2]
    for j in range(m, 2, -1):
        arr2[fresh[1]][j] = arr2[fresh[1]][j-1]
    arr2[fresh[1]][2] = 0

def twoToOne():
    for i in range(1, n+1):
        for j in range(1, m+1):
            arr[i][j] = arr2[i][j]

def printArr(arr):
    for i in range(1, len(arr)): 
        print(" ".join(map(str, arr[i][1:])))

while(t != 0):
    t-=1
    zeroReset()
    allPlace()
    reverseClock()
    clock()
    twoToOne()

for i in range(1, n+1):
    for j in range(1, m+1):
        res+=arr[i][j]

print(res+2)