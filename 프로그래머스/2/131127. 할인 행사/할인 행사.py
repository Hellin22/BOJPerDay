from collections import defaultdict
def solution(want, number, discount):
    
    dt = defaultdict()
    for i, j in zip(want, number):
        dt[i] = j
    res = 0
    l, r = 0, 9
    
    for i in range(9):
        word = discount[i]
        if word in dt: dt[word]-=1 
        
    while r != len(discount):
        if discount[r] in dt: dt[discount[r]]-=1
        
        # 1. dt가 모두 0인지
        flg = True
        for v in dt.values():
            if v != 0:
                flg = False
                break
        if flg: res+=1
        
        if discount[l] in dt: dt[discount[l]] += 1
        l, r = l+1, r+1
    
    return res
    '''
    10일 연속 일치할 경우 회원가입
    윈도우
    discount 0~9까지 want에 추가
    number에 매치되면 ans+1
    
    
    '''