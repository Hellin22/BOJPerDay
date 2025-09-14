from math import sqrt
def solution(n):
    answer = 0
    
    if int(sqrt(n)) < sqrt(n):
        return -1
    else: return (sqrt(n)+1)**2
    