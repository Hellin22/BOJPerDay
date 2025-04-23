'''
그거랑 비슷한데
가장 큰 만들 수 있는 정사각형은 무엇인가?
dp문제
'''


def solution(mats, park):
    answer = 0
    
    n = len(park)
    m = len(park[0])
    arr = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = arr[i][0]
    for j in range(m):
        dp[0][j] = arr[0][j]
        

    num_st = set()
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][j] == 0: continue
            
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + arr[i][j]
            num_st.add(dp[i][j])

    mats.sort(key=lambda x: -x)
    
    for i in mats:
        if i in num_st:
            return i
    
    return -1