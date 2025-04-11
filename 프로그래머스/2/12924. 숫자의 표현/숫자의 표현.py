'''
투포인터
left, right = 0

'''

def solution(n):
    if n == 1: return 1
    answer = 1
    left, right = 1, 1
    summ = left
    while True:
        if summ == n:
            answer+=1
            right+=1
            summ+=right
        elif summ < n:
            right+=1
            if right > n: break
            summ+=right
        else: 
            summ-=left
            left+=1
            
        if left >= right: break
        
        
    return answer