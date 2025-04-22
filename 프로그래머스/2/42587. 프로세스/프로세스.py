'''
결국 우선순위가 가장 높은건지를 알고 있어야함.
우선순위는 최대 9 -> dt에 저장하면 되겠다. (list보다 좋을듯)

'''

import heapq
from collections import deque
def solution(priorities, location):

    cnt = 0
    hq = []
    priorities = deque(priorities)
    for pri in priorities:
        heapq.heappush(hq, -pri)
        
    for i, pri in enumerate(priorities):
        if location == i:
            priorities[i] = [priorities[i], 1]
        else: 
            priorities[i] = [priorities[i], 0]
    
    while priorities:
        if priorities[0][0] == -hq[0]:
            if priorities[0][1] == 1:
                return cnt+1
            else: 
                cnt+=1
                priorities.popleft()
                heapq.heappop(hq)
        else:
            a = priorities.popleft()
            priorities.append(a)
        
        
    return answer