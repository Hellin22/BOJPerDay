import sys
sys.setrecursionlimit(10**6)
inp = sys.stdin.readline

n = int(inp())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    frrom, to = map(int, inp().strip().split())
    graph[frrom].append(to)
    graph[to].append(frrom)


visit = [False] * (n+1)
res = 0
# 1번에서부터 dfs를 돌려도 될거같은데?
def dfs(num, cnt):
    global res
    leaf_flag = True
    for i in graph[num]:
        if not visit[i]:
            # 방문 안했으면 걸로가기
            leaf_flag = False
            visit[i] = True
            dfs(i, cnt+1)
            visit[i] = False
    if leaf_flag: res+=cnt
    # 한번도 방문x -> 그게 리프노드임

visit[1] = True
dfs(1, 0)
print("No" if res % 2 == 0 else "Yes")