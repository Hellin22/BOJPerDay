from collections import Counter

def solution(s):
    answer = True
    
    ct = Counter(s.lower())
    return ct['y'] == ct['p']
