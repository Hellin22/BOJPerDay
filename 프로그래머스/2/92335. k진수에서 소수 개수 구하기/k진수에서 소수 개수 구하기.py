def solution(n, k):
    '''
    같은 소수라도 다른 소수로 체크
    
    양의 정수 n을 k진수로 바꾸는게 첫번째
    
    1. n을 k진수로 변경
    
    2. 어떤 값이 0이 아닌 경우 하나의 string으로 쳐야함.
    -> 0이 나오는 순간 이 값이 10진수로 봤을 때 소수인지 확인
     
    '''
    def ch_to_k(n, k):
        # n을 k진수로 변경
        '''
        11을 3진수
        102
        11 / 3 = 3 ... 2
        3 / 3 = 1 ... 0
        102 -> n%k가 0이 아니라면 반복'''
        sttr = ""
        while n > 0:
            sttr = str(n % k) + sttr
            n //= k
        return sttr
    
    sttr = ch_to_k(n, k)
    count = 0
    
    while len(sttr) != 0:
        tmp_str = ""
        for i in range(len(sttr)):
            if sttr[i] != "0":
                # 0이 아니면 tmp_str에 추가
                tmp_str += sttr[i]
            else:
                # sttr 길이를 줄이기
                sttr = sttr[i+1:] # i가 0이었기 때문에 i+1부터
                if tmp_str == "": break
                
                # 0이면 tmp_str이 소수인지 검증
                tmp_int = int(tmp_str)
                sosu_flag = True
                for j in range(2, int(tmp_int**(0.5))+1):
                    if tmp_int % j == 0: # 소수가 아님
                        sosu_flag = False
                        break
                if sosu_flag and tmp_int not in (0, 1):
                    count+=1
                tmp_str = ""
                break
        
        if tmp_str == sttr and len(sttr) != 0: # 0이 없는 경우 예외처리
            
            tmp_int = int(tmp_str)
            sosu_flag = True
            for j in range(2, int(tmp_int**(0.5))+1):                    
                if tmp_int % j == 0: # 소수가 아님
                    sosu_flag = False
                    break
            if sosu_flag and tmp_int not in (0, 1): 
                count+=1
            break
    
    return count
    
    
    
    
    
    