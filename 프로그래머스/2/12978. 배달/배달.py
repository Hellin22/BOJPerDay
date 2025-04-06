'''
1번 마을에서 각 마을로 음식 배달
k시간 이하로 가능한 마을에서만 주문 받을거임.
다익스트라를 쓸꺼임.

'''
import heapq

def solution(n, road, K):
    answer = 0
    INF = float('inf')
    
    arr = [[] for _ in range(n+1)]
    dist_list = [INF] * (n+1)
    dist_list[1] = 0
    visit = [0] * (n+1)
    
    for frrom, tto, dist in road:
        arr[frrom].append((tto, dist)) # 도착정점, 거리
        arr[tto].append((frrom, dist)) # 양방향 간선이라 2개 다 넣음
    # 1번에서 시작해야함. -> 1번에서 갈 수 있는곳을 전부 넣어줌.
    # 1. 시작정점 추가
    hq = []
    
    for tto, dist in arr[1]:
        if 0 + dist <= K:
            dist_list[tto] = min(dist_list[tto], 0 + dist)
            heapq.heappush(hq, (0+dist, tto))
    while hq: # hq가 빌때까지 진행
        dist_one, node = heapq.heappop(hq)
        
        # node에서 tto로 가야함. -> dist[tto]가 더 작을때만 감
        for tto, dist_two in arr[node]:
            if dist_one + dist_two <= dist_list[tto]:
                if dist_one + dist_two <= K: # k시간보다 작을때만 감.
                    heapq.heappush(hq, (dist_one + dist_two, tto))
                    dist_list[tto] = dist_one + dist_two
                    
    for di in dist_list:
        if di != INF:
            answer+=1
    return answer














