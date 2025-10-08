import sys
inp = sys.stdin.readline
# n개의 라면 공장
# 각 공장은 1번 ~ n번
# i번 공장에서 정확히 ai개 라면 구매 필요

# 아래 세가지 방법으로 라면 구매
# 1. i번 공장에서 라면 하나 구매(3원)
# 2. i, i+1 공장에서 라면 하나씩 구매(5원)
# 3. i, i+1, i+2 공장에서 라면 하나씩 구매(7원)
# 최소 비용으로 라면 구매 -> 필요한 금액은?

# 계속 3개를 보면서 1보다 크면 그렇게 구매하고 아니면 다르게 하면 안되나?

# 3개 처리가 가능한데 중간이 0인 경우는?
# 2 3 2 2

# 0 1 2 2 10원
# 0 0 1 1 17원
# 0 0 0 0 22원

# 0 1 0 2 14원
# 0 0 0 2 17원
# 0 0 0 0 23원

# 즉 2개를 먼저 처리하는게 나을수도 있음
# a[i+1]이 a[i+2]보다 큰 경우를 따로 체크


n = int(inp().strip())
a = list(map(int, inp().strip().split()))
ans = 0
for i in range(n):
    cnt = 0
    if a[i] == 0: continue

    if i+2 <= n-1 and a[i+1] > a[i+2]: # 2개 먼저 처리
        t = min(a[i], a[i+1]-a[i+2])
        a[i]-=t
        a[i+1]-=t
        ans += t*5

    if i+2 <= n-1 and a[i] != 0 and a[i+1] != 0 and a[i+2] != 0 :
        cnt = min(a[i], a[i+1], a[i+2])
        a[i], a[i+1], a[i+2] = a[i]-cnt, a[i+1]-cnt, a[i+2]-cnt
        ans += cnt*7
        ans += a[i]*3
        a[i] = 0

    elif i+1 <= n-1 and a[i] != 0 and a[i+1] != 0:
        cnt = min(a[i], a[i+1])
        a[i], a[i+1] = a[i]-cnt, a[i+1]-cnt
        ans += cnt*5
        ans += a[i]*3
        a[i] = 0
    else:
        cnt = a[i]
        ans += cnt*3
        a[i] = 0

print(ans)