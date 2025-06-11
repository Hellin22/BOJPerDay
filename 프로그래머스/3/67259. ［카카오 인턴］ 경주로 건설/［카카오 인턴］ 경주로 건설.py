'''
arr[i][j]에는 4개가 있음.
arr[i][j][0]은? 동쪽에서 들어온것 => 즉, arr[i][j][k]에서 k 방향으로 i, j까지 들어 왔을 때의 금액을 의미

초기 값들은 10000으로 초기화하고 그걸 큐에다가 넣으면서 진행
만약 i, j, k 모두 동일한데 cost가 동일하다. -> 이러면 진행 x
근데 생각해보니까 방향이 중요한거는 500 이상 차이날때 즉, 코너가 추가되느냐 안되느냐에 따라서 값이 달라질 떄 중요한거라 생각
따라서 5개로 지정해놓기? 동서남북, 최소, 어떤 값이 추가될때 최소를 계속 갱신해주기? 그냥 4방향 모두 봐도 될듯?

근데 그냥 그렇게 하지말고 어떻게될지는 모르는 거니까 4방향 모두 저장해놓고 저거 bfs 진행하기
bfs q 안에 들어가는 것은 (x, y, 방향?) 근데 arr[x][y][dir]의 의미는 dir 방향으로 x, y에 들어왔다는 의미임.
이거 잘 해석해야함.
즉, popleft해서 x, y, dir이 있다면 dir+2를 한 방향으로 보내는게 맞다는 의미(동쪽으로 들어왔으니까 서쪽으로 내보냄)
'''
from collections import deque

def solution(board):
    n = len(board)
    arr = [[[10000000 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    
    dq = deque()
    
    for i in range(4):
        arr[0][0][i] = 0
    
    if board[0][1] == 0: # 0,0 동쪽 갈수 있으면 추가하기
        arr[0][1][2] = 100 # 서쪽에서 들어오는 것이기 때문이다.(큐에 넣을 때에는 방향 "0"으로 설정하기)
        dq.append((0, 1, 0, 100)) # x, y, dir
    if board[1][0] == 0: # 0,0 남쪽 갈 수 있으면 추가하기
        arr[1][0][3] = 100
        dq.append((1, 0, 1, 100)) # 북쪽에서 들어왔고 남쪽 방향유지 (dir+2 %4)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동 남 서 북
    while dq:
        x, y, dr, cost = dq.popleft()
        for ndir, (dx, dy) in enumerate(directions):
            nx, ny = x+dx, y+dy
            ncost = cost
            # nx, ny가 새로운 좌표임. 갈 수 있는지부터 확인하기
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 1: continue # 벽이면 못간다
            
            # 그게 아니라면 갈 수 있다는 의미. 해당 위치로 가는 cost 계산
            # ndir하고 dr이 일치하는지만 확인하면 됨.(뒤로 돌아오는거는 어떻게 계산하는가? 불가능? -> 그것만 빼기)
            # 0이면 2빼기 0 1 3 dr, dr+1, dr+3
            if ndir == (dr+2)%4: continue # 뒤로 돌아가는 경우는 없다.
            if ndir != dr: ncost+=500 # 만약 방향이 동일하지 않다면 코너 만들기
            ncost+=100 # 직선도로 100 추가하기
            if arr[nx][ny][(ndir+2)%4] <= ncost: continue # ncost보다 저 적은 cost로 이미 가능하다? continue
            # dq에 추가할 차례 (cost 비교가 우선 되어야함.)
            # if board[0][1] == 0: # 0,0 동쪽 갈수 있으면 추가하기
            #     arr[0][1][2] = 100 # 서쪽에서 들어오는 것이기 때문이다.(큐에 넣을 때에는 방향 "0"으로 설정하기)
            #     dq.append((0, 1, 0, 100)) # x, y, dir
            # 현재는 ndir로 갈 수 있는것.
            # arr[nx][ny][(ndir+2)%4]를 보고 비교해야함.
            
            arr[nx][ny][(ndir+2)%4] = ncost
            dq.append((nx, ny, ndir, ncost))
    
    return min(arr[n-1][n-1])