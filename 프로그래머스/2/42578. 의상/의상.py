from collections import defaultdict

def solution(clothes):
    dt = defaultdict(int)
    for a, b in clothes:
        dt[b] +=1
    
    ans = 1
    for v in dt.values():
        ans *= (v+1)
    
    return ans-1
    
    
    '''
    개수+1 곱하고 -1
    '''