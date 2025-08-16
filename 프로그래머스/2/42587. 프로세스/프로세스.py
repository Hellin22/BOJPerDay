from heapq import heappush, heappop
from collections import deque
def solution(priorities, location):
    
    # 어떤 놈을 타겟하는지 설정. -> 타켓하는놈은 1로 아닌놈들은 -1로
    # heap으로 처리
    hq = []
    for i in priorities:
        heappush(hq, -i)
    for i in range(len(priorities)):
        if i != location: priorities[i] = [priorities[i], -1]
        else: priorities[i] = [priorities[i], 1]
        
    dq = deque(priorities)
    while dq:
        a, b = dq.popleft() # 현재 프로세스 꺼내기
        # 우선순위가 제일 높은지 확인
        if a == -hq[0]:
            if b == 1: return len(priorities) - len(dq)
            else: heappop(hq)
        
        else: # 우선순위가 제일 안높음
            dq.append([a, b])
    
    '''
    1. 큐에서 대시 프로 하나 꺼냄
    2. 큐에 꺼낸거보다 우선순위 높은거 있으면 다시 큐에 넣음
    3. 없다면? 방금꺼 실행 -> 이 프로세스는 종료
    
    '''
    
    