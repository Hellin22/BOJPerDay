def solution(n):
    answer = 0
    
    x = 2
    while True:
        if n % x == 1:
            return x
        x+=1
    
    
