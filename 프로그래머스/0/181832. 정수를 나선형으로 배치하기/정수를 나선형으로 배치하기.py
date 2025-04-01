'''
1 1 2번 모두 하고나면 종료하면됨.
'''

def solution(n):
    # n이 주어짐.
    num = 1
    arr = [[0] * n for _ in range(n)]
    # n번, n-1 n-1 n-2 n-2 ...
    limit = 1 # 2번 수행할수 있음. limit가 2가되면 n번이 n-1번이 됨.
    cur = 0
    cur_n = n
    
    cur_dir = 0 # 현재 방향. 만약 cur이 cur_n과 같아진다. == cur_dir+1%4
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동 남 서 북
    cur_x, cur_y = 0, 0 # 0, 0에서 시작
    cnt = 0
    while cur_n != 0:
    # while cnt != 11:   
        # print("전",cur_x, cur_y, cur_dir, cur, cur_n)
        
        arr[cur_x][cur_y] = num
        num+=1
        cur+=1
        if cur == cur_n:
            limit+=1
            if limit == 2: # limit가 2가 된다면 하나 줄여야함.
                limit = 0
                cur_n-=1
            cur = 0
            cur_dir = (cur_dir+1) % 4
        cur_x, cur_y = cur_x + directions[cur_dir][0], cur_y + directions[cur_dir][1]
        # print("후",cur_x, cur_y, cur_dir)
        cnt+=1
    print(arr)
    return arr