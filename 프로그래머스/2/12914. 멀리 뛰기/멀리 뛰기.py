def solution(n):
    if n == 1: return 1
    elif n == 2: return 2

    dp = [0] * n
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n):
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567
    return (dp[n-2] + dp[n-1]) % 1234567
    
    '''
    dp[n]
    -> 1, 2칸만 가능함.
    dp[1] = 1
    dp[2] = 2 // 1 1, 2
    dp[3] = 3 // 1 1 1, 1 2, 2 1 
    dp[4] = 5 // dp[3]에서 1칸 더가기 or dp[2]에서 2칸 더가기 -> dp[3]+dp[2]
    '''