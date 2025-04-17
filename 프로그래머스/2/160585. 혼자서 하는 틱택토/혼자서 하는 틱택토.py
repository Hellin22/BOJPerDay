'''
O가 먼저 나온다
즉, O의 개수가 X보다 하나 많거나 같다 -> 이게 아니면 틀린것

1. O의 개수가 X보다 하나 많거나 같다
2. O의 위치, X의 위치 저장 
-> 각각에 대해서 조합적으로 시행?
9개니까 최대 5 4개로 진행 가능함

2. 좌표에 대해서 어떤 좌표인지에 따라 위아래 좌우 살펴보는 코드가 필요함

'''

def solution(arr):
    answer = -1
    
    axy, bxy = [], []
    for i in range(3):
        for j in range(3):
            if arr[i][j] == "O":
                axy.append([i, j])
            elif arr[i][j] == "X" : bxy.append([i, j])
            
    # 1. o가 x보다 1개 많거나 같아야함.
    if not (len(axy) == len(bxy) or len(axy) == len(bxy)+1):
        return 0 
    # 2. xy 좌표에 대해서 좌우, 위아래, 대각선 살피기
    agood, bgood = 0, 0
    for (x, y) in axy:
        if x == 0: # 제일 위쪽에 -> 위아래 확인
            if arr[x+1][y] == arr[x][y]:
                if arr[x+2][y] == arr[x][y]:
                    agood+=1
        if y == 0: # 제일 왼쪽
            if arr[x][y+1] == arr[x][y]:
                if arr[x][y+2] == arr[x][y]:
                    agood+=1
        
        if (x, y) == (0, 0): # 좌상단 대각선
            if arr[x+1][y+1] == arr[x][y]:
                if arr[x+2][y+2] == arr[x][y]:
                    agood+=1
        
        if (x, y) == (2, 0):
            if arr[x-1][y+1] == arr[x][y]:
                if arr[x-2][y+2] == arr[x][y]:
                    agood+=1
    for (x, y) in bxy:
        if x == 0: # 제일 위쪽에 -> 위아래 확인
            if arr[x+1][y] == arr[x][y]:
                if arr[x+2][y] == arr[x][y]:
                    bgood+=1
        if y == 0: # 제일 왼쪽
            if arr[x][y+1] == arr[x][y]:
                if arr[x][y+2] == arr[x][y]:
                    bgood+=1
        
        if (x, y) == (0, 0): # 좌상단 대각선
            if arr[x+1][y+1] == arr[x][y]:
                if arr[x+2][y+2] == arr[x][y]:
                    bgood+=1
        
        if (x, y) == (2, 0):
            if arr[x-1][y+1] == arr[x][y]:
                if arr[x-2][y+2] == arr[x][y]:
                    bgood+=1
                    
    if agood != 0 and bgood != 0:
        return 0
    
    # 만약 agood가 !=0이라면 O가 1개 더 많아야함 항상.
    if agood != 0:
        if len(axy) == len(bxy):
            return 0
        
    # 만약 bgood이 !=0이라면 x와 o 개수가 동일해야함.
    if bgood != 0:
        if len(axy) == len(bxy)+1:
            return 0
    
    return 1