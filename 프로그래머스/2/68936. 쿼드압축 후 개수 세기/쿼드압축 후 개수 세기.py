def solution(arr):
    n = len(arr)
    # 시작점으로 시작하기. 항상 크기가 1/2로 나눠짐
    ans = [0, 0]
    def match(x, y, sec):
        nonlocal n, ans
        if sec == 1:
            ans[0 if arr[x][y] == 0 else 1] += 1 # ans 증가
            return
        
        flag = True
        num = arr[x][y] 
        for i in range(x, x+sec):
            for j in range(y, y+sec):
                if num == arr[i][j]: continue
                else: 
                    flag = False
                    break                
        
        if flag:
            ans[0 if arr[x][y] == 0 else 1] += 1 # ans 증가
        else:
            match(x, y, sec//2)
            match(x, y+sec//2, sec//2)
            match(x+sec//2, y, sec//2)
            match(x+sec//2, y+sec//2, sec//2)
        
    match(0, 0, n)
    
    return ans