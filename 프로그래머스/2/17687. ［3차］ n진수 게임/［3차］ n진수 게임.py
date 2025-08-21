from collections import deque
def solution(n, t, m, p):
    
    
    '''
    n진법, t개의 미리 구할 숫자 수, m명 인원, 튜브 순서p
    
    0 1 10 11 100 101 111 1000
    0 1 1 1
    n 진법으로 바꾸는 방법이 필요 -> t는 1000개 -> 완탐으로도 충분히 가능한 수치
    
    '''
    ans = []
    # 어떤 수 num을 n진법으로 바꾸는 함수
    dq = deque()
    namerji = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'A', '11':'B', '12':'C', '13':'D', '14':"E", '15':"F"}
    
    def change(n, num):
        while num >= n: # 8 // 3 = 2
            dq.appendleft(namerji[str(num%n)])            
            num//=n
        dq.appendleft(namerji[str(num)])
        
    p = p-1 # 내 차례
    cur = 0 # 현재 순서
    num = 0
    while len(ans) < t:
        dq = deque()
        change(n, num) # dq에 값이 들어감
        num+=1
        
        # dq에서 처리하고 cur+=1 -> dq 빌때까지
        while dq and len(ans) < t: # popleft
            pl = dq.popleft()
            if cur == p:
                ans.append(pl)
            cur = (cur+1) % m
    return ''.join(map(str, ans))