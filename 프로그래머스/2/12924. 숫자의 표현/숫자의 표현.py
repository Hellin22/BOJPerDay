'''
n을 연속된 자연수로 표현하는 법

'''
def solution(n):
    if n == 1: return 1
    left, right = 1, 2
    summ = left+right
    cnt = 0
    while left <= right:
        if summ <= n:
            if summ == n: 
                cnt+=1
            right+=1
            summ+=right
        elif summ > n: # n보다 크다면 left 줄이기
            summ -= left
            left+=1
    
    return cnt