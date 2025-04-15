'''
백만개 -> 좌표니까  ^2을 해야할거같은데 이렇게 되면 시간초과
dp?
1~백만
# 일단 내부에 있는거를 dp에 저장해놓을까?
dp[1] = 5 # 길이가 1인 원 (1^2) + 4
dp[2] = dp[1] + (9+4) (3^2) + 4
dp[3] = 25+4 (5^2) + 4
dp[4] = 49+4
n*2-1 ^2

25 - 9 + 4
r2*2-1 ^2 - r1*2-1 ^2 + 4
'''

import math
def solution(r1, r2):
    
    r2_ans = 0
    for i in range (r2-1, 0, -1):
        a = int(math.floor(math.sqrt(r2*r2 - i*i))) 
        r2_ans += a
    r2_ans *=4
    r2_ans += (r2*4)+1
        
    r1_ans = 0
    for i in range(r1-1, 0, -1):
        a = r1*r1 - i*i
        if math.floor(math.sqrt(a)) == math.sqrt(a):
            r1_ans += int(math.floor(math.sqrt(a)))-1
        else: r1_ans += int(math.floor(math.sqrt(a)))
    
    r1_ans *=4
    r1_ans += (r1*4)+1
    
    
    return r2_ans - r1_ans + 4


