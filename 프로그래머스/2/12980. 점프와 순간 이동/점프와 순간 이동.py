'''
n은 1~10억
k는 1이상 자연수  순간이동은 건전지x, k만큼 이동하려면 건전지 k만큼 사용 / 0부터 n까지 가야함
1. 현재 이동거리 x2 만큼 이동가능

'''
from collections import deque
def solution(n):
    ans = 0
    
    while n != 0:
        if n % 2 == 0: # 2로 나누기
            n//=2
        else:
            n-=1
            ans+=1
    
    return ans
    
        
