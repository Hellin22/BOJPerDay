def prime_factorization(N):
    factor = 2  
    while factor * factor <= N:
        while N % factor == 0:
            print(factor)
            N //= factor
        factor += 1
    if N > 1:  
        print(N)

N = int(input())
if N > 1:
    prime_factorization(N)
