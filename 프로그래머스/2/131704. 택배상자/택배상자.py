'''
[4, 3, 1, 2, 5] 이 순서대로 꺼내야함.
기존은 [1, 2, 3, 4, 5] -> 만약 꺼냈는데 안맞다 == 보조에 넣기
언제까지? 나올때까지
즉, 1. 만약 현재 상자 번호가 order[i]보다 작다 == 같을때까지 빼서 order에 넣기
2. 현재 상자 번호가 order[i]보다 크다 == stck[-1]을 보기 -> 안된다? == 불가능
3. stck[-1]이 현재 상자 번호다? == stck.pop 하고 계속 진행
'''
from collections import deque
def solution(order):
    dq = deque()
    order = deque(order)
    for i in range(1, len(order)+1):
        dq.append(i)
    stck = []
    llist = []
    while dq:
        if order[0] > dq[0]:
            while dq and order[0] != dq[0]:
                a = dq.popleft()
                stck.append(a)
            llist.append(order.popleft())
            dq.popleft()
            
        elif order[0] < dq[0]:
            if stck[-1] == order[0]:
                stck.pop()
                llist.append(order.popleft())                
            else: return len(llist)
        else:
            dq.popleft()
            llist.append(order.popleft())
    
    while stck:
        if stck[-1] == order[0]:
            stck.pop()
            llist.append(order.popleft())
        else: return len(llist)
    
    return len(llist)