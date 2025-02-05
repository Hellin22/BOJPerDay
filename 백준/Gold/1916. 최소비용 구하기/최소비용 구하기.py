import sys
import heapq

inp = sys.stdin.readline
v = int(inp())
e = int(inp())

arr = [[] for _ in range(v+1)]
for i in range(e):
    fr, to, weight = map(int, inp().split())
    arr[fr].append([to, weight])

start, end = map(int, inp().split())

pq = []
weights = [123456789] * (v+1) # start에서 갈 수 있는 가중치
heapq.heappush(pq, [0, start]) # 가중치, 정점번호
weights[start] = 0

while pq:
    w, vnum = heapq.heappop(pq)

    if weights[vnum] < w: continue

    for i in range(len(arr[vnum])):
        new_v, new_dist = arr[vnum][i][0], w + arr[vnum][i][1]
        if new_dist >= weights[new_v]: continue
        weights[new_v] = new_dist
        heapq.heappush(pq, [new_dist, new_v])

print(weights[end])