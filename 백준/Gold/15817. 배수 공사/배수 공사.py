import sys
inp = sys.stdin.readline

n, x = map(int, inp().strip().split())

pipes = []
for i in range(n):
    a, b = map(int, inp().strip().split())
    pipes.append((a, b))

dp = [0] * (x+1)
dp[0] = 1 # 길이 0인거는 아무것도 안써서 만들 수 있음.

for length, cnt in pipes:
    for cur_length in range(x, -1, -1):
        for cur_cnt in range(1, cnt+1):
            if cur_length - cur_cnt * length < 0:
                break
            dp[cur_length] += dp[cur_length - cur_cnt * length]

print(dp[x])
