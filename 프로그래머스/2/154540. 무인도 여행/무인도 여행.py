'''
전형적인 bfs?
x가 아니라면 bfs를 돌림 -> 식량 저장할 값 필요 -> bfs의 return 값이 sum_food
이걸 answer.append 해주기

마지막에 sort하는거 잊지말기
'''
from collections import deque
def solution(maps):
    answer = []
    
    n = len(maps)
    m = len(maps[0])    
    visit = [[0] * m for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def bfs(i, j):
        nonlocal n, m
        food_sum = 0
        dq = deque()
        dq.append((i, j))
        visit[i][j] = 1
        while dq:
            x, y = dq.popleft()
            food_sum+=int(maps[x][y])
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0 and maps[nx][ny] != "X":
                    dq.append((nx, ny))
                    visit[nx][ny] = 1
        return food_sum
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and maps[i][j] !="X":
                # int 적용해줘야함.
                answer.append(bfs(i, j))
                print(1)
    if not answer: return [-1]
    
    
    return sorted(answer)
