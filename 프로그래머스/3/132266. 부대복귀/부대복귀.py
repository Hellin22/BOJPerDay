'''
다익스트라?
destination에서 다른 sources 까지의 거리를 구하면 될 거 같다.
'''
from heapq import heappush, heappop
from collections import deque
def solution(n, roads, sources, dest):
    answer = []
    graph = [[] for _ in range(n+1)]
    
    for road in roads:
        a, b = road[0], road[1]
        graph[a].append(b)
        graph[b].append(a)
    
    visit = [-1] * (n+1)
    dq = deque()
    visit[dest] = 0
    dq.append((visit[dest], dest))
    while dq:
        cost, node = dq.popleft()
        for nd in graph[node]:
            if visit[nd] == -1:
                visit[nd] = cost+1
                dq.append((visit[nd], nd))
        
    for sr in sources:
        answer.append(visit[sr])
    
    return answer