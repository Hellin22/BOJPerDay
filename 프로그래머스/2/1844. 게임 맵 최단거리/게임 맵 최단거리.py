from collections import deque
def solution(maps):
    
    n, m = len(maps), len(maps[0])
    
    ans = -1
    
    directions = [[0,1], [1,0],[0,-1],[-1,0]]
    
    dq = deque()
    dq.append((0, 0, 1))
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    while dq:
        x, y, cnt = dq.popleft()
        if (x, y) == (n-1, m-1): return cnt
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or maps[nx][ny] == 0 or visit[nx][ny] == 1 : continue
            dq.append((nx, ny, cnt+1))
            visit[nx][ny] = 1
            
    return ans