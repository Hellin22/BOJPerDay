import math
def solution(n, k):
    
    '''
    n을 k진수로 바꿈 -> 소수가 몇개
    0이 있으면 안됨.
    
    찾은 수가 소수인지 확인하는법?
    1. n을 k진수로 바꾸는 함수 change
    2. 해당 값에서 나온 수의 소수 판별
    '''
    llist = []
    def change(n, k):
        while n >= k:
            llist.append(n%k)
            n//=k
        llist.append(n)
    change(n, k)
    
    cnt = 0
    def is_prime(num):
        nonlocal cnt
        if num <= 1: return False
        for i in range(2, int(math.sqrt(num)+1)):
            # i로 나눠지는지 확인
            if num % i == 0:
                return False
        cnt+=1
        
        
    ss = ''.join(map(str, (llist[::-1])))
    small_ss = ""
    for i in range(len(ss)):
        if ss[i] != '0': small_ss += ss[i]
        else:
            # 0이라면
            if small_ss:
                is_prime(int(small_ss))
            small_ss = ""
    if small_ss:
        print(small_ss)
        print(is_prime(int(small_ss)))
        
    return cnt