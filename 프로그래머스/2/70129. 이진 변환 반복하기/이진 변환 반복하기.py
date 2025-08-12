'''
x의 모든 0 제거
x 길이가 c이면 x는 c가 되고 c를 2진법으로 바꾼걸로 바뀜.
이거 bin?
1이 될때까지 진행
replace 0 ''
'''
def solution(s):
    ans, cnt = 0, 0
    while s != '1':
        cnt+=1
        
        # 1. s의 모든 0 제거
        ans += len(s) - len(s.replace('0', ''))
        s = s.replace('0', '')
        
        # 2. s의 길이를 다시 s에 대입
        s = bin(len(s))[2:]
    return [cnt, ans]