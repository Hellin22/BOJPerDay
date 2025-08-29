from collections import deque
def solution(maps):
    '''
    직사각형, nm
    통로만 가능
    시작 -> 레버
    레버 -> 출구
    가능한 시간 / -1
    '''
    n, m = len(maps), len(maps[0])
    sx, sy, ex, ey, lx, ly = -1, -1, -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                sx, sy = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
    
    dq = deque()
    visit = [[0] * m for _ in range(n)]
    dq.append((sx, sy, 0))
    ans = -1
    fir_flag = False
    while dq:
        x, y, cnt = dq.popleft()
        if maps[x][y] == "L":
            fir_flag = True
            ans = cnt
            break
            
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)): # 0 4
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1 or maps[nx][ny] == "X": continue
            visit[nx][ny] = 1
            dq.append((nx, ny, cnt+1))
            
    if not fir_flag: return -1

    dq = deque()
    visit = [[0] * m for _ in range(n)]
    dq.append((lx, ly, 0))
    while dq:
        x, y, cnt = dq.popleft()
        if maps[x][y] == "E":
            return ans+cnt
        
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] == 1 or maps[nx][ny] == "X": continue
            visit[nx][ny] = 1
            dq.append((nx, ny, cnt+1))
    
    return -1