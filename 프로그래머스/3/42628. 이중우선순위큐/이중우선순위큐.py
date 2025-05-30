'''
기존에 생각한 방식 = heapq 2개 유지(최대, 최소힙)
dt를 통해서 숫자 유무, 개수 유지
최대값 삭제 = 최대힙, 최소도 마찬가지
if 최대값의 top이 dt에 없다. == 이미 없는 값 == 아무것도 안하고 진행

but, 이렇게 진행하면 느리다. + 연산이 엄청 많아지면 시간초과도 가능

-> 자꾸 이렇게 풀라고 하길래 일단 해보자. 다른사람 풀이보고 다른 방법 찾아보자.
'''

from heapq import heappush, heappop

def solution(operations):
    answer = []
    
    hq_min = []
    hq_max = []
    
    dt = dict()
    cnt = 0
    for ops in operations:
        a, b = ops.split(" ")
        if a == "I":
            heappush(hq_min, int(b))
            heappush(hq_max, -int(b))
            dt[int(b)] = dt.get(int(b), 0) + 1
            cnt+=1   
        else: # a == "D"
            if cnt == 0: continue
            if int(b) == 1:
                # 최대값 삭제 -> hq_max에서 삭제
                while hq_max:
                    mx = -heappop(hq_max)
                    
                    if dt[mx] != 0:
                        cnt-=1
                        dt[mx]-=1
                        # if dt[mx] == 0:
                        #     del dt[mx]
                        break
            else: # 최소값 삭제
                while hq_min:
                    mn = heappop(hq_min)
                    
                    if dt[mn] != 0:
                        cnt-=1
                        dt[mn]-=1
                        # if dt[mn] == 0:
                        #     del dt[mn]
                        break
                        
        
    if cnt == 0: # 비어있으면
        return [0, 0]

    # 안비어있으면 실제 최대, 최소값을 찾아야함.
    mx, mn = -1, -1
    while dt[-hq_max[0]] == 0:
        heappop(hq_max)
    mx = -hq_max[0]
    while dt[hq_min[0]] == 0:
        heappop(hq_min)
    mn = hq_min[0]

    return [mx, mn]