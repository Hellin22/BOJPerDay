def solution(m, n, board):
    ans = 0
    '''
    nm은 30까지
    확인은 오른쪽, 아래만 확인하기
    들어있는 값이 -1이면 확인하지 않기 -> 0은 빈자리 의미
    m, n
    '''
    arr = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # R M A F N T J C
            arr[i][j] = board[i][j]
    
    while True:
        # 1. 사라질 위치들 찾기
        erase_st = set()    # 사라질 위치 저장하는 set
        # visit = [[0] * n for _ in range(m)] # 방문 했는지 여부
        for i in range(m):
            for j in range(n):
                # visit[i][j] = 1
                if arr[i][j] == -1: continue # 비어있으면 그대로
                else: # 안비어있다면 01 10 11 찾아보기.
                    flag = True
                    for dx, dy in ((0,1), (1,0), (1,1)):
                        nx, ny = i+dx, j+dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n or arr[nx][ny] != arr[i][j]:
                            flag = False
                            break
                    if flag: # flag면 4면이 같음
                        # 1. st에 추가
                        # 2. visit 했다고 표시 -> visit을 굳이?
                        for dx, dy in ((0,1), (1,0), (1,1), (0, 0)):
                            erase_st.add((i+dx, j+dy))
        pans = ans
        # 2. 사라질 위치 찾았으니 삭제해주고 ans+=1
        for x, y in erase_st:
            arr[x][y] = -1
            ans+=1
            
        if pans == ans: break # ans 안늘어났으면 종료
        
        # 3. 이모티콘들 내리기
        for i in range(m-2, -1, -1): # 0번 위치도 해줘야함.
            for j in range(n):
                # i를 내려야함. -> if arr[di][j] == -1이라면, di가 m보다 작다면
                di = i+1 # 한칸 밑으로 내려가야 하기 때문
                while di < m and arr[di][j] == -1: # di가 m-1이라면 제일 밑바닥에 내린다는 의미
                    arr[di][j] = arr[di-1][j]
                    arr[di-1][j] = -1 # 한칸 내려서 비어있음
                    di+=1
    return ans