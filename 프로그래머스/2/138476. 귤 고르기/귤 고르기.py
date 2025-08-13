from heapq import heappush, heappop
def solution(k, tangerine):
    
    hq = []
    a = [0] * 10000001
    for i in tangerine:
        a[i]+=1
    for i in a:
        if i != 0:
            heappush(hq, -i)
    ans = 0
    while hq and k > 0:
        
        k-= -heappop(hq)
        ans+=1
    return ans        
    '''
    k개를 골라 상자 하나에 담아 판매
    크기별로 분류 -> 크기가 가장 작은걸로?
    heap?
    '''