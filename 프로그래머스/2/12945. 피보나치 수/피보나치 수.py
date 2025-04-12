def solution(n):
    answer = 0
    
    fibo_list = [0] * (n+1)
    fibo_list[0] = 0
    fibo_list[1] = 1
    fibo_list[2] = 1
    fibo_list[3] = 2
    
    for i in range(2, n+1):
        fibo_list[i] = (fibo_list[i-1] + fibo_list[i-2]) % 1234567
    
    return fibo_list[n]