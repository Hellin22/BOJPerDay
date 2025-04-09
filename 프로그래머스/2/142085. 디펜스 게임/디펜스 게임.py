'''
n	k	        enemy	          result
7	3	[4, 2, 4, 5, 3, 3, 1]	    5
2	4	     [3, 3, 3, 3]	        4

n은 남은 병사수 10억
k는 무적권 개수 5십만
enemy는 라운드마다의 적의 수 / enemy의 길이는 백만 / 각 적의 수는 백만
result는 최대 막을 수 있는 라운드 수

다시 생각해보자.
pq의 한번 연산은 얼마의 시간이 들까?
어떠한 수를 pq에 넣는 연산은 log n이 듦
따라서 log1 log2 ... log n임.
이걸 다 합쳐도 1~ log 백만 -> 백만은? 1000000 -> 2^10 (1000)000 -> 40임.
즉, 1~40까지 백만개가 있고 그 사이에 값들은 절대로 3천만을 넘지 않음.
pq로 하는거 맞는거같음.

for i, power in enumerate(enemy):
    if n - power >= 0:
        heapq.heappush(hq, power)
        n-=power
    elif n-power < 0: 
        
        # k가 0이 아니라면 -> k가 0이면 못함. k가 0이면 현재 i 리턴하면 됨.
        # hq에서 최대값 하나를 뺌 -> 현재가 더 크다면 못함. -> break
        if hq[0] <= power: break
        a = heapq.heappop(hq)
        n+=a
        k-=1
        heapq.heappush(hq, power)

'''
import heapq
def solution(n, k, enemy):
    answer = 0
    hq = []
    for i, power in enumerate(enemy):
        if n - power >= 0: # 집어넣을 수 있는 경우 의미 (무적권 안씀)
            heapq.heappush(hq, -power)
            n-=power
            
            
            
        elif n-power < 0: # 해당 라운드를 못함. -> 무적권 쓸 수 있는지 확인하기
            # 만약 무적권이 있다면 hq[0]랑 power중 큰거를 무적권 쓰고 넘겨야함.
            
            if k == 0: return i # 남은 무적권이 없으면 종료
            

            # 무적권이 있으면 hq[0]에 쓸찌 powe에 쓸지 -> hq가 비어있다면?
            if not hq: # 무적권이 있는데 hq가 비어있어서 power에 무적권 쓰기
                k-=1
            elif hq: # 무적권이 있고 hq 안에 원소가 있음. 둘중 어디쓹지 확인
                if -hq[0] > power: # 빼냈으니까 power를 집어넣어야함.
                    a = heapq.heappop(hq)
                    n+=a*-1
                    heapq.heappush(hq, -power)
                    n-=power    
                # else: # power가 더 커서 넣지 못함.
                    
                    
                k-=1
            
            
    return len(enemy)