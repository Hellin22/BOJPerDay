import sys
import heapq
inp = sys.stdin.readline

v, e = map(int, inp().strip().split())

# 1과 v -> 1에서 v로 가야함

arr = [[] for _ in range(v+1)]
for i in range(e):
    fr, to, we = map(int, inp().strip().split())
    arr[fr].append([to, we])
    arr[to].append([fr, we])

dist = [123456789] * (v+1)
dist[1] = 0
pq = []
heapq.heappush(pq, [0, 1])
while pq:
    curDist, curVertex = heapq.heappop(pq)
    if curDist > dist[curVertex]: continue
    for i in range(len(arr[curVertex])):
        newDist, newVertex = curDist + arr[curVertex][i][1], arr[curVertex][i][0]
        if newDist >= dist[newVertex]: continue
        heapq.heappush(pq, [newDist, newVertex])
        dist[newVertex] = newDist

print(dist[v])