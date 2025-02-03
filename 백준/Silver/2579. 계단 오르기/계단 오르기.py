import sys
inp = sys.stdin.readline

a = int(inp())

scores = [0] + [int(inp()) for _ in range(a)]

# 마지막 계딴은 무조건 밟아야함
# 연달아 3개는 안됨
# 한칸 or 두칸 오르기 가능
score = 0
dp = [[0] * (a+1) for _ in range(2)]
if a == 1:
    print(scores[1])
    exit()

dp[0][1] = 0
dp[1][1] = scores[1]
dp[0][2] = scores[2]
dp[1][2] = scores[1]+scores[2]

for j in range(3, a+1):
    dp[0][j] = max(dp[0][j-2], dp[1][j-2]) + scores[j]
    dp[1][j] = dp[0][j-1] + scores[j]

print(max(dp[0][a], dp[1][a]))