'''
n은 효진이가 도달해야할 좌표
효진이는 1, 2만 가능
즉, 1과 2를 무한개 사용해서 n 만드는 개수를 리턴 -> %1234567
dp네 -> dp[i]는 i를 만드는 개수합
'''
def solution(n):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    
    return dp[n]