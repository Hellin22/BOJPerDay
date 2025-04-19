from collections import deque
import math
def solution(n, stations, w):
    answer = 0
    
    # n은 2억 -> 모두 다 보려고하면 안됨.
    # w가 1이라면? 
    stations = deque(stations) # deque로 변경
    
    cur = 1

    while cur <= n:
        if not stations:
            if n-cur == 0: answer+=1
            else: answer += math.ceil((n-cur)/(2*w+1))
            break
        if stations[0]-w > cur:
            answer+=1
            cur = cur+2*w+1
        else: 
            cur = stations[0]+w+1
            stations.popleft()

    
    return answer