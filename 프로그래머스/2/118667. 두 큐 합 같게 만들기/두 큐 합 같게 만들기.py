from collections import deque
def solution(queue1, queue2):
    
    '''
    작은거에서 큰걸로 원소를 옮기면 됨. 가능할때까지.
    불가능하다면? -1
    언제 불가능하지? 
    cnt가 len+len이 된다면 불가능?
    '''
    
    d1 = deque(queue1)
    d2 = deque(queue2)
    
    cnt = 0
    d1s = sum(d1)
    d2s = sum(d2)
    MAXIMUM = len(d1) + len(d2)*2
    while cnt <= MAXIMUM and d1s != d2s:
        if d1s > d2s: # d1s에서 빼고 d2s에 넣기
            pop_num = d1.popleft()
            d1s-=pop_num
            d2s+=pop_num
            d2.append(pop_num)
        else:
            pop_num = d2.popleft()
            d2s-=pop_num
            d1s+=pop_num
            d1.append(pop_num)
        cnt+=1
        
    return cnt if cnt <= MAXIMUM else -1