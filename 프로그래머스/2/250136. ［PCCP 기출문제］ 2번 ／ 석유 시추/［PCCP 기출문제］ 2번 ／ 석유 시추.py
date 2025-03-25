from collections import deque
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cur_num = 1
def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    for i in range(n):
        for j in range(m):
            land[i][j] = [0, land[i][j]]
            
    visit = [[0] * m for _ in range(n)] 
    for i in range(n):
        for j in range(m):
            if land[i][j][1] == 1 and visit[i][j] == 0:
                land, visit = bfs(i, j, land, visit, n, m)

    for j in range(m):
        answer = max(answer, check(j, n, land))
    return answer

def bfs(x, y, llist, visit, n, m):
    global cur_num
    
    dq = deque()
    dq.append((x, y))
    visit[x][y] = 1
    ch_list = []
    ch_list.append((x, y))
    while dq:
        kx, ky = dq.popleft()
        for dx, dy in directions:
            nx, ny = kx + dx, ky + dy
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0 and llist[nx][ny][1] == 1:
                visit[nx][ny] = 1
                dq.append((nx, ny))
                ch_list.append((nx, ny))
                
    for x, y in ch_list:
        llist[x][y] = (cur_num, len(ch_list))
    cur_num+=1
    return llist, visit

def check(j, n, llist):
    res = 0
    st = set()
    for i in range(n):
        if llist[i][j][0] not in st and llist[i][j][1] != 0:
            res+=llist[i][j][1]
            st.add(llist[i][j][0])
    
    return res