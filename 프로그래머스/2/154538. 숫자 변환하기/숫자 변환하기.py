from collections import deque
def solution(x, y, n):
    
    '''
    x -> y로 만드는 최소 연산 횟수
    2x, 3x, x+n
    불가능하면 -1
    '''
    if x == y: return 0

    dq = deque()
    visit = [0] * 1000001
    for i in [3*x, 2*x, x+n]:
        if i == y: return 1
        elif i <= 100000 and i < y:
            dq.append((i, 1))
            visit[i] = 1
            
    while dq:
        a, cnt = dq.popleft()
        if a > y: continue
        elif a == y: 
            return cnt
        else:
            for i in [3*a, 2*a, a+n]:
                if i <= 1000000 and i <= y and visit[i] == 0: 
                    dq.append((i, cnt+1))
                    visit[i] = 1
                    
    return -1