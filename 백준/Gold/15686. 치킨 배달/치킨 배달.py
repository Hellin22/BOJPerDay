import sys
from collections import deque
inp = sys.stdin.readline

n, m = map(int, inp().strip().split(" "))

arr = [[0] * n for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
chickenPlace = []
curChickenPlace = []
housePlace = []
res = 2501

def chickenPick(idx, cnt):
    if cnt == m:
        bfs()
        return
    
    for i in range(idx, len(chickenPlace)):
        curs = chickenPlace[i]
        arr[curs[0]][curs[1]] = 2
        curChickenPlace.append([curs[0], curs[1]])
        chickenPick(i+1, cnt+1)
        arr[curs[0]][curs[1]] = 0
        curChickenPlace.pop()

def bfs():
    global res
    cnt = 0
    for i in range(len(housePlace)):
        minCnt = 2501
        for j in range(len(curChickenPlace)):
            minCnt = min(minCnt, 
            (abs(curChickenPlace[j][0] - housePlace[i][0]) + abs(curChickenPlace[j][1] - housePlace[i][1])))
        cnt += minCnt

    res = min(res, cnt)

for i in range(n):
    llist = list(map(int, inp().strip().split()))
    for j in range(len(llist)):
        arr[i][j] = llist[j]
        
        if arr[i][j] == 2:
            arr[i][j] = 0
            chickenPlace.append([i, j])
        elif arr[i][j] == 1:
            housePlace.append([i, j])

chickenPick(0, 0)
print(res)

# 1. 치킨집 중에 m개 고르기
# 2. housePlace에 대해서 반복문 돌리기 (visit 배열 초기화)
# 3. res 갱신
