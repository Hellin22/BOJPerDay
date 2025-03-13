import sys
inp = sys.stdin.readline

n = int(inp())
llist = list(map(int, inp().strip().split()))

dp = [-1] * n

dp[0] = 0

for i in range(n):
    if dp[i] == -1: continue
    for j in range(1, llist[i]+1):
        if i+j >= n or dp[i+j] != -1: continue
        dp[i+j] = dp[i] + 1

print(dp[n-1])