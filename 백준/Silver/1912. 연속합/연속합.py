import sys
inp = sys.stdin.readline

n = int(inp())
arr = list(map(int, inp().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
print(max(dp))