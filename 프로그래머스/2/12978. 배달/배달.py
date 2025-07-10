from heapq import heappush, heappop

def solution(n, road, K):
    # 마을개수 n, 도로 road, k시간
    # 1번마을에서 시작
    
    graph = [[] for _ in range(n+1)]
    for a, b, dist in road:
        graph[a].append((dist, b))
        graph[b].append((dist, a))
        
    hq = []
    dst = [10000000000000] * (n+1)
    dst[1] = 0 # 1번마을은 dist 0
    heappush(hq, (0, 1))
    
    while hq:
        dist, node = heappop(hq)    
        
        if dist > dst[node]: continue
        
        for d, a in graph[node]:
            if dist + d > dst[a]: continue
            else:
                heappush(hq, (dist+d, a))
                dst[a] = dist+d
    
    print(dst)
    answer = 0
    for di in dst:
        if di <= K:
            answer+=1
    return answer
    
    