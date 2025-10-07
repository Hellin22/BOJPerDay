import sys
inp = sys.stdin.readline

# N개의 집
# XI YI가 주어지는데 XI가 y값이고 YI가 X값으로 생각
N, K = map(int, inp().strip().split()) # n은 50개 최대, k는 3개
llist = []

# 집에서 가장 가까운 대피소로 이동할때 가장 긴 거리가 최소가 되도록
# k개의 대피소를 n개중에 정할것


# i번째 집과 j번째 집 사이의 거리는 x차이 + y차이
for i in range(N):
    y, x = map(int, inp().strip().split())
    llist.append((x, y))

# n개중 k개를 결정하기
# 그 k개에서 다른 모든 집까지의 거리 구하기
# 그 중에서 max 값들을 모두 모음.
# 그 중에서 min값
# 집까지의 거리 차이를 dp로 구성해놓기

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if i == j: continue

        # dp[i][j]는 i에서 j까지의 거리
        dp[i][j] = abs(llist[i][0] - llist[j][0]) + abs(llist[i][1] - llist[j][1])
        dp[j][i] = dp[i][j]


# 1. N개 중 K개 선택하기
llist2 = []
minn, maxx = 987654321, -1
def dfs(idx):
    global N, K, maxx, minn
    if len(llist2) == K:
        # maxx값 구하기
        # llist2에 있는 위치와 다른 대피소와의 거리 중 최대값 구하기
        maxx = find_max()
        minn = min(maxx, minn)

        return
    
    # llist2에 하나 추가하기. 순서가 중요하지 않은 조합
    for i in range(idx+1, N):
        llist2.append(i)
        dfs(i)
        llist2.pop()

# llist2에 있는 대피소와 다른 곳들의 거리 중 최대값 찾기
def find_max():
    global maxx, N
    
    maxx = -1

    for i in range(N):
        tmp_minn = 987654321
        for j in llist2:
            # i에서 j대피소까지 걸리는 거리 중 최소값
            tmp_minn = min(tmp_minn, dp[i][j])
        maxx = max(maxx, tmp_minn)

    return maxx

dfs(-1)
print(minn if N != K else 0)