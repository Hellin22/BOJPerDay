import sys
inp = sys.stdin.readline

n = int(inp().strip()) # 도시의 개수
dist = list(map(int, inp().split()))
cost = list(map(int, inp().split()))
# dist[i]에서는 ~cost[i]의 최소값을 선택하면 됨.
minCost = cost[0]
res = minCost * dist[0]
for i in range(1, n-1):
    minCost = min(minCost, cost[i])
    res += minCost * dist[i]

print(res)