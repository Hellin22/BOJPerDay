from collections import deque
def solution(places):
    '''
    대기실은 5개 5*5
    응시자 끼리는 맨해튼거리 2 이하로 앉으면 안됨 (3부터 가능)
    파티션으로 막혀있으면 오케이
    
    -> 사람마다 bfs 돌면서 맨해튼거리 2 이하의 사람이 있는지 확인
    맨해튼 거리 = 좌표 뺀거 절대값 합
    '''
    ans = []
    for k in range(5):
        flag = True
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == "P":
                    dq = deque()
                    dq.append((i, j, 0))
                    visit = [[0]*5 for _ in range(5)]
                    visit[i][j] = 1
                    while dq:
                        if not flag: break
                        x, y, cnt = dq.popleft()
                        if cnt == 2: continue
                        for dx, dy in ((1, 0), (-1,0), (0, 1), (0, -1)):
                            nx, ny = x+dx, y+dy
                            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or visit[nx][ny] == 1 or places[k][nx][ny] == "X": continue
                            
                            if places[k][nx][ny] == "P":
                                ans.append(0)
                                flag = False
                                break
                                
                            visit[nx][ny] = 1
                            dq.append((nx, ny, cnt+1))
        if flag: ans.append(1)    
    return ans