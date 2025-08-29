from heapq import heappush, heappop
def solution(n, road, k):
    '''
    출발, 도착, 거리
    음식배달 가능한 시간 = k
    
    1번 마을에서 배달
    '''
    graph = [[] for _ in range(n+1)]
    
    for fr, to, dist in road:
        graph[fr].append((to, dist))
        graph[to].append((fr, dist))
    
    INF = 987654321
    dists = [INF] * (n+1)
    hq = []
    
    heappush(hq, (0, 1)) 
    dists[1] = 0
    
    while hq:
        dist, node = heappop(hq)
        
        if dists[node] < dist: continue
        
        for i in range(len(graph[node])):            
            if graph[node][i][1] + dist > dists[graph[node][i][0]]: continue
            
            heappush(hq, (graph[node][i][1]+dist, graph[node][i][0]))
            dists[graph[node][i][0]] = graph[node][i][1]+dist

    return len([i for i in dists if i <= k])
        