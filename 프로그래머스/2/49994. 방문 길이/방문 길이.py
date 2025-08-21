def solution(dirs):
    
    '''
    처음 걸어본 길의 길이 구하기
    점을 배열로 잡기
    00 ~ -5-5 55 5-5 
    11개 크기
    
    
    '''
    map = [[[0] * 4 for _ in range(11)] for _ in range(11)] # 0은 안간것 -> 4개의 방향이 있음. 고려해주기
    
    x, y = 5, 5
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dt = {'R':0, 'D':1, 'L':2, 'U':3}
    cnt = 0
    for i in dirs:
        dx, dy = directions[dt[i]][0], directions[dt[i]][1]
        nx, ny = x+dx, y+dy
        if nx < 0 or ny < 0 or nx >= 11 or ny >= 11: continue
        if map[x][y][dt[i]] == 0:
            map[x][y][dt[i]] = 1
            map[nx][ny][(dt[i] +2)%4]=1
            cnt+=1
        x, y = nx, ny
    
    return cnt