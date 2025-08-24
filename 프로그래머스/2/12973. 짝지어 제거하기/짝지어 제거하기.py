def solution(s):
    stck = []
    for i in s:
        if not stck: stck.append(i)
        else: #
            if stck[-1] == i:
                stck.pop()
            else: stck.append(i)
    return 1 if not stck else 0
    
    
    
    
    
    
    
    
    
    '''
    소문자 문자열
    같은 알파벳 2개 짝 -> 삭제 후 이어붙임
    문자열 모두 제거 -> 종료
    가능 유무를 1, 0
    
    완탐은 안될듯
    이거 어캐풀지? ㅋㅋ
    abcddcba
    3 4
    abccba
    
    left-1, left로 가면 되나?
    
    스택?ㅇㄴㅇㅇㅇㅇ
    '''