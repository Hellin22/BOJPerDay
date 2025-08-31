from collections import deque
def solution(arr):
    '''
    X 1~9
    X는 바다
    숫자는 무인도
    
    무인도 없으면 -1
    있으면 오름차순
    
    그냥 일반 BFS?
    '''
    
    n, m = len(arr), len(arr[0])
    ans = []
    for i in range(n):
        arr[i] = list(arr[i])
    for i in range(n):
        for j in range(m):
            if arr[i][j] != "X":
                dq = deque([(i, j, int(arr[i][j]))])
                fin_cnt = int(arr[i][j])
                arr[i][j] = "X"
                while dq:
                    x, y, cnt = dq.popleft()
                    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        nx, ny = x+dx, y+dy
                        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == "X": continue
                        dq.append((nx,ny,cnt+int(arr[nx][ny])))
                        fin_cnt = fin_cnt + int(arr[nx][ny])                        
                        arr[nx][ny] = "X"
                ans.append(fin_cnt)
                
    return sorted(ans) if ans else [-1]