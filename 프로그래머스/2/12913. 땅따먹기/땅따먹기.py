'''
dp 배열 -> 땅따먹기 하면서 점수 총합 저장 0번째 행은 land[0][j]
'''

def solution(land):
    answer = 0
    dp = [[0] * 4 for _ in range(len(land))]
    for j in range(4):
        dp[0][j] = land[0][j]
    
    for i in range(1, len(dp)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][:j]+ dp[i-1][j+1:]) + land[i][j]
    return max(dp[len(land)-1])