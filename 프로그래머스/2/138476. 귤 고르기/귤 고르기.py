from collections import Counter
def solution(k, tangerine):
    
    ct = Counter(tangerine)
    llist = sorted(list(ct.values()), key = lambda x: -x)
    for i, cnt in enumerate(llist):
        k-=cnt
        if k <= 0:
            return i+1
    
    '''
    k개를 골라 상자 하나에 담아 판매
    크기별로 분류 -> 크기가 가장 작은걸로?
    heap?
    '''