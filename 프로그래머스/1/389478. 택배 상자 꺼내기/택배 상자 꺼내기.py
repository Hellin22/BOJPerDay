def solution(n, w, num):
    answer = 0
    
    arr = [[0] * 100 for _ in range(100)]
    cur_n = 1 # 현재까지의 택배 상자 개수
    # w는 가로 개수(col의 개수)
    
    curx, cury = 0, 0
    arr[curx][cury] = cur_n
    cur_n+=1
    while cur_n <= n:
        # 언제 위로 올라가는가? cury가 0이나 w-1일때
        # curx가 0일때는 ->임 즉, curx % 2 == 0이라면 오른쪽으로감
        # -> 따라서 cury+=1이 되고 만약 cury가 w-1이다. 그러면 
        # curx+=1임.
        
        # curx % 2 == 1 이라면 왼쪽으로 가는것
        # 만약 cury가 0이라면 curx+=1
        # 그게 아니라면 cury-=1
        
        # curx가 1일때는 <-임
        if curx%2 == 0:
            if cury == w-1:
                curx+=1
            else: 
                cury+=1
        else:
            if cury == 0:
                curx+=1
            else:
                cury-=1
        
        arr[curx][cury] = cur_n
        # print(curx, cury, cur_n, arr[curx][cury])
        cur_n+=1
    
    for i in range(100):
        for j in range(10):
            print(i, j, arr[i][j])
            if arr[i][j] == num:
                # 그 위에 0이 아닌걸 찾기
                curi = i+1
                res = 1
                while True:
                    if arr[curi][j] != 0:
                        curi+=1
                        res+=1
                    else:
                        return res
    return answer