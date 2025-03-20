n = int(input().strip())

llist = [list(map(int, input().strip().split())) for _ in range(n)]
# 1. up, down, right, left 메서드 구현하기
res = 0

def copy_list(llist2): # llist2가 llist꺼를 저장함함
    global n
    for i in range(n):
        for j in range(n):
            llist2[i][j] = llist[i][j]

def recover_list(llist2): # llist가 llist2 내용물을 가져옴
    global n
    for i in range(n):
        for j in range(n):
            llist[i][j] = llist2[i][j]

def update_res():
    global n, res
    for i in range(n):
        for j in range(n):
            res = max(res, llist[i][j])

def dfs(cnt):
    global res, n
    if cnt == 5:
        # 25번 돌면서 res 갱신
        update_res()
        return

    llist2 = [[0] * n for _ in range(n)]
    # llist2 = llist하기
    copy_list(llist2)
    # print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    up()
    dfs(cnt+1)
    # llist를 llist2로 변경하기기
    recover_list(llist2)

    copy_list(llist2)
    # print("dddddddddddddddddddddd")
    down()
    dfs(cnt+1)
    recover_list(llist2)

    copy_list(llist2)
    # print("rrrrrrrrrrrrrrrrrrrrrrrrr")
    right()
    dfs(cnt+1)
    recover_list(llist2)
    
    copy_list(llist2)
    # print("llllllllllllllllllllllllllll")
    left()
    dfs(cnt+1)
    recover_list(llist2)

def up():
    global n
    for j in range(n):
        i = 1
        is_ch = 0
        while i < n:
            # print(i, "최초 i")
            # printt()
            # print("프린트 함 해야지지")
            if llist[i][j] == 0:
                i+=1
                continue
            elif llist[i][j] != 0:
                tmp_i = i-1
                while True:
                    if tmp_i == -1: break
                    if llist[tmp_i][j] != 0: break
                    tmp_i-=1
                # print("현재 i는", i, "현재 tmpi는", tmp_i)
                if tmp_i == -1: # tmp_i가 -1 이라는 의미 = 젤 위로 올리면됨
                    llist[0][j] = llist[i][j]
                    llist[i][j] = 0
                else: # tmp_i가 -1이 아니라는거는 0이 아닌거를 만났다는것
                    if llist[tmp_i][j] == llist[i][j] and is_ch == 0:
                        llist[tmp_i][j] = llist[tmp_i][j]*2
                        llist[i][j] = 0
                        is_ch = 1
                    elif llist[tmp_i][j] != llist[i][j] or is_ch == 1:
                        is_ch = 0
                        if tmp_i+1 != i:
                            llist[tmp_i+1][j] = llist[i][j]
                            llist[i][j] = 0
                i+=1
                # print(i)
def down():
    global n
    for j in range(n):
        i = n-2
        is_ch = 0
        while i >= 0:
            # print(i, "최초 i")
            # printt()
            # print("프린트 함 해야지지")
            if llist[i][j] == 0:
                i-=1
                continue
            elif llist[i][j] != 0:
                tmp_i = i+1
                while True:
                    if tmp_i == n: break
                    if llist[tmp_i][j] != 0: break
                    tmp_i+=1
                # print("현재 i는", i, "현재 tmpi는", tmp_i)
                if tmp_i == n: # tmp_i가 -1 이라는 의미 = 젤 위로 올리면됨
                    llist[n-1][j] = llist[i][j]
                    llist[i][j] = 0
                else: # tmp_i가 -1이 아니라는거는 0이 아닌거를 만났다는것
                    if llist[tmp_i][j] == llist[i][j] and is_ch == 0:
                        llist[tmp_i][j] = llist[tmp_i][j]*2
                        llist[i][j] = 0
                        is_ch = 1
                    elif llist[tmp_i][j] != llist[i][j] or is_ch == 1:
                        is_ch = 0
                        if tmp_i-1 != i:
                            llist[tmp_i-1][j] = llist[i][j]
                            llist[i][j] = 0
                i-=1
                # print(i)

def right():
    global n
    for i in range(n):
        j = n-2
        is_ch = 0
        while j >= 0:
            if llist[i][j] == 0:
                j-=1
                continue
            elif llist[i][j] != 0:
                tmp_j = j+1
                while True:
                    if tmp_j == n: break
                    if llist[i][tmp_j] != 0: break
                    tmp_j+=1
                if tmp_j == n: # tmp_i가 -1 이라는 의미 = 젤 위로 올리면됨
                    llist[i][n-1] = llist[i][j]
                    llist[i][j] = 0
                else: # tmp_i가 -1이 아니라는거는 0이 아닌거를 만났다는것
                    if llist[i][tmp_j] == llist[i][j] and is_ch == 0:
                        llist[i][tmp_j] = llist[i][tmp_j]*2
                        llist[i][j] = 0
                        is_ch = 1
                    elif llist[i][tmp_j] != llist[i][j] or is_ch == 1:
                        is_ch = 0
                        if tmp_j-1 !=j:
                            llist[i][tmp_j-1] = llist[i][j]
                            llist[i][j] = 0
                j-=1
                # print(i)


def left():
    global n
    for i in range(n):
        j = 1
        is_ch = 0
        while j < n:
            if llist[i][j] == 0:
                j+=1
                continue
            elif llist[i][j] != 0:
                tmp_j = j-1
                while True:
                    if tmp_j == -1: break
                    if llist[i][tmp_j] != 0: break
                    tmp_j-=1
                if tmp_j == -1: # tmp_i가 -1 이라는 의미 = 젤 위로 올리면됨
                    llist[i][0] = llist[i][j]
                    llist[i][j] = 0
                else: # tmp_i가 -1이 아니라는거는 0이 아닌거를 만났다는것
                    if llist[i][tmp_j] == llist[i][j] and is_ch == 0:
                        llist[i][tmp_j] = llist[i][tmp_j]*2
                        llist[i][j] = 0
                        is_ch = 1
                    elif llist[i][tmp_j] != llist[i][j] or is_ch == 1:
                        is_ch = 0
                        if tmp_j+1 != j:
                            llist[i][tmp_j+1] = llist[i][j]
                            llist[i][j] = 0
                j+=1


def printt():
    global n
    print("*************^*^**")
    for i in range(n):
        for j in range(n):
            print(llist[i][j], end = " ")
        print()
    print("************")

dfs(0)
print(res)

'''
4
8 8 8 8
4 4 4 4
2 2 2 2
2 2 2 2

4
4 4 4 4
0 0 0 0
2 2 2 0
2 2 2 4

4
2 2 2 2
2 2 2 2
4 4 4 4
8 8 8 8
'''
