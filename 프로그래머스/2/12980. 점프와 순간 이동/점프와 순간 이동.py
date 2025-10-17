from collections import deque
def solution(n):
    # 0에서 n까지 가야함. -> k칸 점프 == k만큼의 건전지 사용
    # 현재 거리 * 2의 위치로 순간이동 가능
    
    # n은 10억 이하의 자연수
    
    # n을 0으로 만들기
    # 만약 홀수면 1 빼주기, 짝수면 //2 해주기
    ans = 0
    while n != 0:
        if n % 2 == 0: # 짝수
            n //= 2
        else: 
            n-=1
            ans+=1
            
    return ans