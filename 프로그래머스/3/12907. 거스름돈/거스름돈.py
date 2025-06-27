'''
dp[i]는 i원을 만들 수 있는 방법
if m in money:
    dp[m] = 1
for i in range(len(money)):
    # i원 보다 작은 돈
    if money[i] < cur: # cur보다 money[i]가 작으면? 
        cur - money[i]  # 5 - 2 -> 3
        dp[cur] += dp[cur-money[i]]
'''
def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in money:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[n]