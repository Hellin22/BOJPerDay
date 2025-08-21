from heapq import heappush, heappop, heapify

def solution(scoville, k):
    
    '''
    맵지 않은거 + 2번째 맵지않은거 *2 
    
    모든 음식의 스코빌을 k 이상으로 만들기 -> heap[0]가 k 이상이면 됨
    '''
    heapify(scoville)
    
    cnt = 0
    while len(scoville) >= 2 and scoville[0] < k: # hq가 있고 k를 못넘는다면
        a, b = heappop(scoville), heappop(scoville)
        heappush(scoville, a+b*2)
        cnt+=1
        
    if not scoville or scoville[0] < k: # hq 없거나 k 이상으로 못만들면
        return -1
    else: return cnt