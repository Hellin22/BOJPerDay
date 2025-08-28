from collections import deque
import math
def solution(players, m, k):
    '''
    m명 늘어날때마다 서버+1
    어느 시간대 이용자가 n*m명 이상 (n+1)*m 미만 -> n대는 가동중이어야함
    
    m이 3이면?
    증설된거니까 9, 10, 11명은 3대 서버 증설로 감당 가능함.
    즉, 증설 서버 +1 * m이 최대 수용수 의미
    
    한번 증설한 서버는 k 시간 동안만 가능
    k가 5이면 10~15까지만 운영
    
    '''
    
    dq = deque() # 서버가 언제까지 켜놓아지는지를 저장하는 덱
    # [종료시간, 서버대수]
    cnt = 0 # 현재 서버 대수
    ans = 0 # 답
    for i, p in enumerate(players):
        
        
        if dq and dq[0][0] == i: # 증설된 서버 삭제
            cnt-=dq.popleft()[1]
        
        need = p//m # 필요한 서버 수 의미
        
        # 필요한 서버수보다 cnt가 많다? 그러면 증설 안해도됨.
        # 필요한 서버수가 cnt보다 많다? 그러면 필요한 서버수-cnt만큼 dq에 추가해야함.
        # cnt도 증가시키고
        if need <= cnt: continue
        else: 
            dq.append((i+k, need-cnt))
            ans += need-cnt
            cnt = need

    return ans