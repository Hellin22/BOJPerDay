'''
dp 배열 -> 땅따먹기 하면서 점수 총합 저장 0번째 행은 land[0][j]
'''

def solution(land):
    answer = 0
    dp = [[0] * 4 for _ in range(len(land))]
    for j in range(4):
        dp[0][j] = land[0][j]
    
    for i in range(1, len(dp)):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][2]
        dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][3]
    return max(dp[len(land)-1][0], dp[len(land)-1][1], dp[len(land)-1][2], dp[len(land)-1][3])