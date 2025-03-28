from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    a = Counter(tangerine)
    
    a = list(a.values())
    a.sort(reverse = True)
    for i, val in enumerate(a):
        answer+=val
        if answer >= k:
            return i+1
