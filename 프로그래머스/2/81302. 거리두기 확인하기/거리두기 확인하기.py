'''
맨해튼 거리가 2 이하면 안됨.
파티션이 있으면 가능
근데 맨해튼거리 상에 파티션이 있어도 단 하나라도 빈책상(O)가 있으면 안됨.ㅇ

[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
각각 따로임.
[1, 0, 1, 1, 1]


행길이 = 5, 세로도 5
완탐해야할듯?
모든 P를 구하기 -> 맨해튼 거리가 3이면 가능하네??
즉, 어떠한 사람(X, Y)에 대해서 BFS 돌리는데
O이면 가능함.
맨해튼 거리가 2가 될때까지 진행
만약 3이다 == 종료
만약 cnt가 3이 아닌데 p를 만났다. -> 해당 places에서는 불가능 (return 0)
만약 X다 -> 종료
'''
from collections import deque
def solution(places):
    answer = []
    n = len(places)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def bfs(idx):
        nonlocal n
        for i in range(n):
            for j in range(n):
                if places[idx][i][j] == "P":
                    visit = [[0] * n for _ in range(n)]
                    dq = deque()
                    dq.append((i, j, 0))
                    visit[i][j] = 1
                    while dq:
                        x, y, cnt = dq.popleft()
                        if cnt == 2: continue # 2였다면 현재 이미 끝난거임.
                        for dx, dy in directions:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<n and 0<=ny<n:
                                if visit[nx][ny] == 1: continue
                                if places[idx][nx][ny] == "P": 
                                    answer.append(0)
                                    return False
                                    # print(i, j, nx, ny)
                                if places[idx][nx][ny] == "O":
                                    dq.append((nx, ny, cnt+1))
                                    visit[nx][ny] = 1
        answer.append(1)
        return True
                                
                                
    
    for i in range(len(places)):
        print(places[i])
        bfs(i)
    
    
    
    
    return answer