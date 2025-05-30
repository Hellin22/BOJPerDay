from heapq import heappush, heappop
from collections import deque
def solution(n, edge):
    answer = 0
    
    # 1번 노드에서 가장 멀리 떨어진 노드 개수(1번이 시작)
    graph = [[] for _ in range(n+1)]
    for fr, to in edge:
        graph[fr].append(to)
        graph[to].append(fr)
    
#     hq = []
#     INF = float('inf')
#     dist = [INF] * (n+1)
#     heappush(hq, (0, 1)) # dist, node (1->1로 가는 경우)
#     dist[1] = 0
    
    # 다익스트라?... -> bfs로도 가능할거같다.
#     while hq:
#         cur_dist, node = heappop(hq)
        
#         if dist[node] >= cur_dist: 
    
    dist = [0] * (n+1)
    dq = deque()
    dq.append((1, 0))
    
    while dq:
        nm, cnt = dq.popleft()
        for to in graph[nm]:
            if dist[to] != 0: continue
            dist[to] = cnt+1
            dq.append((to, cnt+1))

    answer = dist.count(max(dist)) if max(dist) != dist[1] else dist.count(max(dist))-1
    
    return answer