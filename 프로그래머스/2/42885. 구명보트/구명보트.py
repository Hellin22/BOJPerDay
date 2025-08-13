from collections import deque
def solution(people, limit):
    
    dq = deque(sorted(people, key=lambda x: -x))
    ans = 0
    while dq:
        if len(dq) >= 2 and dq[0] + dq[-1] <= limit:
            dq.popleft()
            dq.pop()
        else: dq.popleft()
        ans+=1
    return ans
    '''
    한번에 최대 2명 + 무게제한
    
    보트 최대한 적게 사용하기
    
    최소 최대를 하나씩 태워보기?
    
    1 3 5 7 9 -> 최대 이다?
    
    2명이니까 최대 최소끼리 태우기?
    
    '''
    
    