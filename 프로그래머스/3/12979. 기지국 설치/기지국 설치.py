import math
def solution(n, stations, w):
    answer = 0
    
    cur = 1
    for idx in stations:
        if idx-w-1 >= cur:
            answer += math.ceil((idx-w-cur) / (2*w+1))
            
        cur = idx+w+1
        
    if cur <= n:
        answer+=math.ceil((n-cur+1)/(2*w+1))
        
        
    return answer