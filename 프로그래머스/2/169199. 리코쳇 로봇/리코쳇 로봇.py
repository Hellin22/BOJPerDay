'''
visit 배열은 방향에 따라서 해놓을까?
일단 dfs를 써야하는거같음.
초기 방향은 상관없는거같음. -> 갈 수 있는 모든곳으로 일단 보내기

board가 100이네... 가능한가?
일단 해보자.
["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
["DGR", "...", "..."]
기댓값 〉 1
'''

from collections import deque
def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동 남 서 북
    def bfs(xx, yy):
        nonlocal n, m
        visit = [[[0] * 4 for _ in range(m)] for _ in range(n)]
        dq = deque()
        dq.append((0, xx, yy))
        # x, y에 대해서 bfs를 시작할꺼임.
        # 갈 수 있는 최대한을 보낼거임.
            
        
        visit_st = set()
        visit_st.add((xx, yy))
            
        while dq:
            ttime, x, y = dq.popleft()
            flag = True
            for i in range(len(directions)):
                nx, ny = x, y
                # 그냥 nx, ny를 계속해서 쭉 늘리자.
                for j in range(1, 100):
                    nx, ny = x+directions[i][0] * j, y+directions[i][1]*j
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "D": break  
                
                nx, ny = nx-directions[i][0], ny-directions[i][1]
                                
                # 안바뀐거임 -> 못감
                if nx == x and ny == y: 
                    continue
                
                if (nx, ny) in visit_st:
                    continue
                
                # 한칸이라도 갈 수 있는것 -> 만약 그곳이 G라면 종료지점임.
                else:
                    if board[nx][ny] == "G":
                        print(ttime+1)
                        return ttime+1
                    visit_st.add((nx, ny))
                    
                    
#                     for kk in range(x, nx+1):
#                         for kkkk in range(y, ny+1):
#                             visit[kk][kkkk][i] = 1
                    
                    dq.append((ttime+1, nx, ny))
        return -1
        
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                return bfs(i, j)
                break
    
    
    
    return answer