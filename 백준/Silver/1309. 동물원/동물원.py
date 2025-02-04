import sys
inp = sys.stdin.readline

a = int(inp())

dp = [0] * a
if a == 1:
    print(3)
    exit()
elif a == 2:
    print(7)
    exit()
dp[1] = 3
dp[2] = 7
for i in range(3, a):
    dp[i] = dp[i-1]*2 + dp[i-2]
    dp[i]%=9901
print((dp[a-1]*2+dp[a-2])%9901)