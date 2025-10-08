import sys
from heapq import heappush, heappop
inp = sys.stdin.readline

# 쉬운디..?

# n, m, k, x
n, m, k, x = map(int, inp().strip().split())

graph = [[] for _ in range(n+1)]
answer = [] # 오름차순 출력
INF = 987654321
dist_list = [INF] * (n+1)
dist_list[x] = 0
for i in range(m):
    # 도로 정보 a -> b
    a, b = map(int, inp().strip().split())
    graph[a].append(b)

# x가 시작점. x에서부터 다른 정점까지의 최소값 찾기
hq = []
hq.append((0 ,x)) # 거리, x
while hq:
    dist, num = heappop(hq)
    
    # 결국 dist에서 추가로 가야하는데 이미 더 적은 값으로 num에 갈 수 있으면 진행x
    if dist > dist_list[num]: continue

    for n_num in graph[num]: # num에서 갈 수 있는 곳들
        if dist + 1 >= dist_list[n_num]: continue

        dist_list[n_num] = dist+1
        heappush(hq, (dist+1, n_num))

for i in range(1, n+1):
    if dist_list[i] == k:
        answer.append(i)

answer.sort()
print('\n'.join(map(str, answer)) if answer else -1)