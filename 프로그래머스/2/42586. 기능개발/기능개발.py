from collections import deque
def solution(progresses, speeds):
    
    ans = []
    dq = deque()
    # 현재 날짜 -> 1일 2일 3일 ...
    cur = 1
    
    for a, b in zip(progresses, speeds):
        dq.append((a, b))
        
    while dq: 
        if dq[0][0] + dq[0][1] * cur < 100:
            cur+=1
        else:
            cnt = 0
            while dq and dq[0][0]+dq[0][1]*cur >= 100:
                dq.popleft()
                cnt+=1
            ans.append(cnt)
    
    return ans