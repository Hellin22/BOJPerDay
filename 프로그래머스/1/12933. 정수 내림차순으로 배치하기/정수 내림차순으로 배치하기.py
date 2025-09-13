def solution(n):    
    return int(''.join(sorted(list(str(n)), key = lambda x: -int(x))))
