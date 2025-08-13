def solution(n,a,b):
    cnt = 0
    while not (abs(a - b) == 1 and a //2 != b //2):
        cnt+=1
        a, b = a//2+a%2, b//2+b%2
    return cnt+1
    '''
    a, b는 언제 만나나?
    1. 1 2 / 3 4 / 5 6 -> 1 / 2 / 3   //2 + %2
    -> a - b = abs(1)이고 a//2 b//2는 달라야함.
    
    '''