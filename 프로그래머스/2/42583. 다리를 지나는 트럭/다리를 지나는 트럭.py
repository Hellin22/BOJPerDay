from collections import deque

def solution(bridge_length, weight, trucks):
    '''
    모든 트럭이 다리 건너려면 최소 몇초
    최대 bridge_length대 가능
    무게는 최대 weight -> 걸친 트럭은 무시
    '''
    dq = deque()    
    trucks = deque(trucks)
    
    cur_time = 0 # dq에 집어넣을때 (truck, time) 집어넣기 -> truck 무게를 같이 넣어줘야하는가? -> 뺄때 그만큼 감소시켜야하기 때문
    weights = 0 # 총 트럭 무게
    while trucks or dq: # trucks가 존재한다면
    # while cur_time != 2:
        cur_time+=1
        
        # dq and cur_time-dq[1] == bridge_length 라면 빼도되는 경우
        if dq and cur_time - dq[0][1] == bridge_length:
            weights-=dq[0][0]
            dq.popleft()

        if len(dq) < bridge_length: # 1대 추가로 올라갈 수 있는 경우
            if trucks and trucks[0] + weights <= weight: # 버틸 수 있다면
                weights += trucks[0]
                dq.append((trucks.popleft(), cur_time))
        
    return cur_time