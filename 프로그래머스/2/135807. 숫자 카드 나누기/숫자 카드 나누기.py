def solution(arra, arrb):
    '''
    가장 큰 양의 정수?
    
    a를 모두 나누면서 b는 못나누는거
    
    b를 모두 나누면서 a는 못나누는거
    
    a의 최대공약수 -> 최대공약수가 나눠지면 그 최대공약수의 약수로 나누기? 
    하지만 최대공약수로 나눠진다는 거는 그 약수에도 나눠진다는 의미
    
    즉, a의 최대공약수로 b를 나눌 수 있는가? or 그 반대 -> 이 과정은 해봐야하는거인듯?
    나눠지면 0
    둘중 큰거
    
    최대공약수는 어캐구하는가? -> gcd(gcd(gcd(...)))
    
    35 // 14 = 2 ... 7
    14 // 7 = 2 ... 0
    
    36 // 14 = 2 ... 8
    14 // 8 = 1 ... 6
    8 // 6 = 1 ... 2
    6 // 2 = 3 ... 0 -> %값이 0이 나올때의 b값
    '''
    def gcd(a, b):
        while a%b != 0:
            bb = a%b
            
            a = b
            b = bb
        return b
    
    arra.sort(reverse=True)
    arrb.sort(reverse=True)
    
    ga, gb = arra[0], arrb[0]
    for i in range(1, len(arra)):
        ga = gcd(ga, arra[i])
    for i in range(1, len(arrb)):
        gb = gcd(gb, arrb[i])
    flaga = True if ga != 1 else False
    flagb = True if gb != 1 else False
    
    if ga != 1:
        for i in arrb:
            if i % ga == 0:
                flaga = False
                break
    
    if gb != 1:
        for i in arra:
            if i % gb == 0:
                flagb = False
                break
                
    if flaga and flagb:
        return max(ga, gb)
    elif flaga:
        return ga
    elif flagb:
        return gb
    else: return 0