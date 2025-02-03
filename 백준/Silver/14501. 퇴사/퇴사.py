import sys
inp = sys.stdin.readline

cnt = int(inp())
ti, pi = [0] * cnt, [0] * cnt
dp = [0] * (cnt+1)
for i in range(cnt):
    a, b = map(int, inp().strip().split())
    ti[i] = a
    pi[i] = b

for i in range(cnt):
    dp[i] = max(dp[i-1], dp[i])
    if i+ti[i] > cnt: continue

    dp[i+ti[i]] = max(dp[i+ti[i]], dp[i] + pi[i])
    if i - 1 < 0: continue
    dp[i + ti[i]] = max(dp[i+ti[i]] , dp[i-1])

print(max(dp[cnt], dp[cnt-1]))