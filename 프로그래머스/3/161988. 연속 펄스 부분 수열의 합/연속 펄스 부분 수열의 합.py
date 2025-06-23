'''
최대한 많은 부분이 양 음 순서로 교차되는 최대의 길이를 구하는 것.
길이는 500,000 -> n^2은 안됨.

무조건 음수, 양수 교차되는 곳을 선택해야하는 것은 아님.
양수 하나가 최대값일 수 있음

결국 dp를 써서 하는게 맞는 방법인듯
0. 연속 부분수열 -> 현재부터 시작할지. 아니면 본인부터 시작할지
고려해야할거는 양수, 음수가 나눠져 있다는 것.
dp[i]는 i번째 일때 최대값
dp[i][0] dp[i][1] 2개로 나누기?? [0]은 내 순번에 -1을 곱할때
[1]은 내 순번에 1을 곱할때 

dp[i][0]은 dp[i-1][1] or sequence[i]*-1 -> max
dp[i][1]은 dp[i-1][0] or sequence[i] -> max

'''
def solution(sequence):
    answer = -100000
    n = len(sequence)
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = sequence[0]*-1
    dp[0][1] = sequence[0]
    
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], 0) - sequence[i]
        dp[i][1] = max(dp[i-1][0], 0) + sequence[i]
    for i in range(n):
        for j in range(2):
            answer = max(answer, dp[i][j])
    return answer