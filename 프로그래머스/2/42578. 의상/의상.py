from collections import Counter

def solution(clothes):
    ct = Counter(k for v, k in clothes)
    ans = 1
    for v in ct.values():
        ans *= (v+1)
    return ans-1