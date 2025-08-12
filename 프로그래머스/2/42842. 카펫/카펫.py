def solution(brown, yellow):
    
    ga, se = brown//2+2, 0
    while True:
        ga, se = ga-1, se+1
        if (ga-2) * (se-2) == yellow:
            return ga, se
    
    
    '''
    brown, yellow 개수 알때 가로 세로 길이는?
    수학문제
    총 개수 = brown + yellow = 가로 * 세로
    3 4 2 1
    가로-2 * 세로-2 = yellow
    가로 * 세로  - yellow = brown
    가세 - 가세 + 2가 + 2세 - 4 = brown
    
    2가 +2세 -4 = brown
    
    가+세-2 = brown//2+2
    
    brown//2+2를 하고 가세 대입해서 yellow와 맞는지 확인. (가로 >= 세로)
    '''