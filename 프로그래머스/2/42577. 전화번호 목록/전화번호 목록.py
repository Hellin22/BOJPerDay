def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    st = set()
    for pb in phone_book:
        for i in range(1, len(pb)+1):
            if pb[:i] in st:
                return False
        st.add(pb)
            
            
    return True
    
    '''
    어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
    
    총 전화번호 1 ~ 백만
    각 전화번호 1~20
    400 백만
    4억?
    
    '''
    return answer