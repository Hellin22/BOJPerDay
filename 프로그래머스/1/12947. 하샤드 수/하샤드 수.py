def solution(x):
    return False if x % sum(map(int, list(str(x)))) else True 
