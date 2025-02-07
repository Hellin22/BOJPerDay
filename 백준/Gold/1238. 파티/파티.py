import sys
import heapq
inp = sys.stdin.readline

'''
일단 x마을(학생)에서 다익스트라 진행.
1번부터 다익스트라를 진행 -> x까지의 거리가 있을꺼임
이때, 제일 처음 x까지의 거리 갱신하기(res = x[1][0]+x[1][1])
그 다음부터 거리의 최단거리(pq에서 뽑은 값)가 res보다 크면 그건 안되는거니까 빼기
'''
v, e, x = map(int, inp().strip().split())

arr = [[] for _ in range(v+1)]

for i in range(e):
    fr, to, we = map(int, inp().strip().split())
    arr[fr].append([to, we])

# 1. x에서부터 다익스트라 진행
fromX = [123456789] * (v+1)

pq = [[0, x]] # 가중치, 정점번호
fromX[x] = 0
heapq.heapify(pq)
while pq:
    curWeight, curVertex = heapq.heappop(pq)
    if fromX[curVertex] < curWeight: continue

    for i in range(len(arr[curVertex])):
        newWeight, newVertex = curWeight + arr[curVertex][i][1], arr[curVertex][i][0]
        if newWeight > fromX[newVertex]: continue
        fromX[newVertex] = newWeight
        heapq.heappush(pq, [newWeight, newVertex])


# x를 제외한 모든 정점에서 다익스트라 돌리기
# 새로운 배열 만들어야함. arr[i][j]에는 i에서 j까지의 거리가 저장되어있음.
# curMin
curMin = -1
toX = [[123456789] * (v+1) for _ in range(v+1)]

for i in range(1, v+1):
    if i == x: continue

    # i에 대해서 다익스트라 진행
    pq =[[0, i]]
    toX[i][i] = 0
    heapq.heapify(pq)
    while pq:
        curWeight, curVertex = heapq.heappop(pq)
        if toX[i][curVertex] < curWeight: continue
        
        for j in range(len(arr[curVertex])):
            newWeight, newVertex = curWeight + arr[curVertex][j][1], arr[curVertex][j][0]
            if newWeight > toX[i][newVertex]: continue
            toX[i][newVertex] = newWeight
            heapq.heappush(pq, [newWeight, newVertex])

maxx = -1
for i in range(1, v+1):
    if i == x: continue
    maxx = max(maxx, fromX[i] + toX[i][x])

print(maxx)