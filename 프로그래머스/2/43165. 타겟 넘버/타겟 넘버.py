from collections import deque

def solution(numbers, target):
    answer = 0
    
    dq = deque()
    dq.append(numbers[0])
    dq.append(-numbers[0])

    for i in range(1, len(numbers)):
        llist = list(dq) # 1하고 -1이 들어있는것 -> 이거에 대해서 numbers[i]를 더하고 빼주는 로직이 필요함.
        for j in range(len(llist)):
            dq.popleft()
            dq.append(llist[j] + numbers[i])          
            dq.append(llist[j] - numbers[i])          
    
    llist = list(dq)
    for i in llist:
        if i == target:
            answer+=1
    
            
    return answer