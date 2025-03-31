'''
일단 q1, q2의 각각의 합, 모든 합을 구해야함.
모든 합 절반이 목표치니까 q1, q2중 더 큰값에서 이걸 빼면 될듯?
종료 -1 조건이 애매했는데, 문제 조건은 길이가 같은 queue1,2임. 
따라서 전체 합이 홀수가 아니라면 len(q)가 0이 되지 않는 이상 모두 가능한거같음
'''
from collections import deque
def solution(q1, q2):
    max_cnt = len(q1)
    q1 = deque(q1)
    q2 = deque(q2)
    q1Sum = sum(q1)
    q2Sum = sum(q2)
    res_cnt = 0
    res = q1Sum + q2Sum
    if res%2 != 0: return -1 # 홀수이면 불가능
    for i in range(max_cnt*3):
        if q1Sum == q2Sum:
            return res_cnt
        elif q1Sum > q2Sum: # q1에서 빼서 q2에 주기
            popNum = q1.popleft()
            q1Sum-=popNum
            q2.append(popNum)
            q2Sum+=popNum
        elif q1Sum < q2Sum: # q2에서 빼서 q1에 주기
            popNum = q2.popleft()
            q2Sum-=popNum
            q1.append(popNum)
            q1Sum+=popNum
        res_cnt+=1
    return -1