from collections import deque

def solution(n):
    
    dq = deque()
    # 반대로 n에서 2분의 1씩 줄이기?
    dq.append((n, 0))
    ans = 0
    while n != 0:
        if n % 2 == 0: # n이 2로 나눠지면
            n//=2
        else: 
            ans+=1
            n-=1
    
    return ans
    '''
    K칸 점프, *2 이동
    이동은 건전지 안들고 점프는 K만큼 듦
    N까지 가려고함
    건전지 사용량 제일 적은 방법
    처음 위치는 0부터 시작
    
    + 되는거만 존재 -> N을 벗어나면 추가 X
    BFS는 DEQUE로
    '''