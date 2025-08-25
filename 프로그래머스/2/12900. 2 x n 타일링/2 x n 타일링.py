def solution(n):
    
    '''
    dp
    dp[1] = 1
    dp[2] = 1 / 1 = 2
    dp[3] = 3
    dp[4] = 5
    '''
    dp = [0] * 60001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%1000000007
    return dp[n]