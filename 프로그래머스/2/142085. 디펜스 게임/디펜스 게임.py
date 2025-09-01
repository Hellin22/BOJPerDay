from heapq import heappush, heappop

def solution(n, k, enemy):
    '''
    n명으로 적 공격 막기
    남은 병사중 enemy[i]만큼 소모해 enemy[i]만큼 막을 수 있음
    "무적권"을 쓰면 병사 소모 없이 막을 수 있음.
    최대 k번
    7 1 1 1 1 1
    무적권 1번이고 체력 8
    dp? 무적권은 최대 500,000개 -> 백만과 오십만.. 메모리 초과
    
    1. 계속해서 체력을 소모하면서 진행
    2. enemy에 대해서 체력을 소모하지 못한다 
    -> heapq에서 최대값을 빼냄 == 무적권으로 해당 적 퇴치
    -> k-=1, 체력+=heappop
    '''
    
    hq = []
    for i, val in enumerate(enemy):
        if n >= val: # 현재 체력으로 적 퇴치 가능
            n-=val
            heappush(hq, -val)
        elif n < val and k > 0: # 퇴치 불가능 -> 무적권 사용 고려
            k-=1
            # 1. hq.top과 val중에 무적권 사용할곳이 어딘지 고려
            if hq and -hq[0] > val: # hq에 무적권 사용해야함.
                n-=heappop(hq) # 음수로 들어가있으니까 마이너스
                heappush(hq, -val)
                n-=val
        else: # 무적권 사용 못함.
            return i
    return len(enemy)