def solution(board):
    '''
    visit을 3차원으로 구성하기 -> 들어오는거를 기준으로 색칠해주기
    동남서북 
    
    visit을 3차원 구성할 필요가 있는가?
    1. 동남서북 한 방향으로 쭉 가기(D나 범위 벗어날때까지)
     -> 이때 VISIT은 ? -> VISIT 한 곳을 다시 갈 수 있음.
     VISIT은 범위 벗어나거나 근처가 벽인 경우에만 VISIT 고려해도 될거같음
      -> 스쳐지나가는 경우는 상관없음. 하지만 똑같은 위치(벽)에 의해 가로막힌다? 이전에 했던거를 그대로 다시하는 경우.
      따라서 D와 범위 벗어나는거에만 적용하기. -> 즉, 더이상 못가는 경우에만 VISIT 하기
      
     2. 최소값이니 결국 완탐 -> 이전껄로 돌아가는 방법? 이전에 어떤 방향으로 왔는지를 모름.
     따라서 이걸 저장해놓고 APPEND, POP 하기. -> 출발지 위치를 저장해놓으면 될듯?
     멈추게됨 -> 출발(X,Y)를 LLIST에 저장 후 NX, NY에 대해서 다시 DFS 진행(FOR문 4방향으로)
        만약 불가능하다. 그러면 RETURN 하고 다시 FOR문으로 돌아오는데 이때 X, Y 알고있잖아...
        굳이 안저장해도 될거같음. ㅇㅇㅇㅇㅇ 그냥 MINN만 잘 조절해서 하면 될듯
    '''
    
    n, m = len(board), len(board[0])
    rx, ry, gx, gy = -1, -1, -1, -1
    # 시작점(rx, ry) 구하기
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                rx, ry = i, j
            elif board[i][j] == "G":
                gx, gy = i, j
    
    visit = [[-1] * m for _ in range(n)]
    directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
    minn = 987654321
    
    def dfs(x, y, cnt):
        nonlocal minn
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx, ny = nx+dx, ny+dy
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == "D":
                    nx, ny = nx-dx, ny-dy
                    break
                
            if board[nx][ny] == "G":
                minn = min(minn, cnt+1)
            elif visit[nx][ny] == -1 or visit[nx][ny] > cnt+1:
                visit[nx][ny] = cnt+1
                dfs(nx, ny, cnt+1)
            
        
        
    dfs(rx, ry, 0)
    return minn if minn != 987654321 else -1