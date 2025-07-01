'''
1000 * 1000
내구도 = 최대 1000
skill 길이 = 250,000
skill의 각 행은 [type, r1, c1, r2, c2, degree]형태
type이 1 -> 적, type이 2 = 회복
degree만큼 줄어들거나 늘어남.

이거 완탐으로는 못품. 최악의 경우 1,000,000 * 250,000
-> 누적합으로 풀 수 있을거같긴한데 어떻게 하지?
2차원 누적합을 어떻게 푸는가?
'''
def solution(board, skill):
    
    n, m = len(board), len(board[0])
    answer = n*m
    
    # 이거 n+2, m+2로 구성 -> 실제 i, j 값은 +1, +1로
    dp = [[0] * (m+2) for _ in range(n+2)]
    # for i in range(n):
    #     for j in range(m):
    #         dp[i+1][j+1] = board[i][j]
    # skill의 각 행은 [type, r1, c1, r2, c2, degree]형태
    for type, r1, c1, r2, c2, degree in skill:        
        if type == 1: degree *= -1
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1
        dp[r1][c1] += degree
        dp[r1][c2+1] -= degree
        dp[r2+1][c1] -= degree
        dp[r2+1][c2+1] += degree
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] += dp[i][j-1]
    for j in range(1, m+1):
        for i in range(1, n+1):
            dp[i][j] += dp[i-1][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += dp[i+1][j+1]
            if board[i][j] <= 0: answer-=1
    
    return answer