import sys
import heapq
inp = sys.stdin.readline

# 일단 가중치가 1이 아니니까 bfs를 못쓴다.
INF = 123456789
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
t = 0
while True:
    '''
    1. 다익스트라를 사용해야함.
    2. 갈 수 있는 곳을 넣어야하는데 
    3. 그냥 상하좌우를 넣으면 되지 않나?
    4. 일단 dist 배열도 최소값을 넣어놔야하고 이차원 배열로 만들어야함.
    5. 2차원 dist -> INF로 초기화 1e9
    6. 0, 0을 집어넣고 만약 거기서 n-1, n-1이 나오면 종료
    '''
    n = int(inp())
    if n == 0: break
    t+=1

    arr = [list(map(int, inp().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    pq = []
    heapq.heappush(pq, [arr[0][0], 0, 0]) # 가중치, x, y
    dist[0][0] = arr[0][0]
    while pq:
        curDist, curx, cury = heapq.heappop(pq)
        if curx == n-1 and cury == n-1: break

        if curDist > dist[curx][cury]: continue

        for i in range(4):
            nx, ny = curx + dx[i], cury + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or dist[nx][ny] <= curDist + arr[nx][ny]: continue
            heapq.heappush(pq, [curDist + arr[nx][ny], nx, ny])
            dist[nx][ny] = curDist + arr[nx][ny]
    print(f"Problem {t}: {dist[n-1][n-1]}")