import heapq

def solution(k, score):
    answer = []
    hq = []
    
    for i in range(len(score)):
        if len(answer) < k:
            heapq.heappush(hq, score[i])
        else:
            if hq[0] < score[i]:
                heapq.heappop(hq)
                heapq.heappush(hq, score[i])
        answer.append(hq[0])
        
    return answer