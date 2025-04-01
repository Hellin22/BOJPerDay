'''
n m h 
세로선, 가로선, 가로선 놓을 수 있는 위치치

m개의 줄에는 가로선의 정보
아 h가 i임
그니깐 이카면됨. m, garo, n
'''
res = 100
m, garo, n = map(int, input().strip().split())
llist = []
sadari = [[[0] * 2 for _ in range(m)] for _ in range(n)] # n*m*2로 진행

for i in range(garo):
    x, y = map(int, input().strip().split())
    x, y = x-1, y-1
    # a, b -> b, b+1을 a행에서 연결했다는 의미?
    sadari[x][y][1], sadari[x][y+1][0] = 1, 1 # 사다리가 있다는 의미ㅣ


def check(): # 모든 사다리가 시작과 도착 열이 같아야함.
    global n, m
    for j in range(m):
        curj = j
        for i in range(n):
            if sadari[i][curj][0] != 0:
                # 사다리가 왼쪽 오른쪽 한군데에 무조건 있음
                # 현재는 왼쪽에 사다리가있으니 curj-=1
                curj-=1
            elif sadari[i][curj][1] != 0:
                # 오른쪽에 사다리가 있으니까 curj+=1
                curj+=1

        if curj != j:
            return False
    
    return True


def make_sadari(curCnt, wantCnt, idxi, idxj): # 현재 사다리 개수, 목표 개수
    global n, m, res

    if curCnt == wantCnt:
        if check(): # 성공임 -> 가능하면 res 갱신
            print(wantCnt)
            exit()
        return

    # 오른쪽만 신경쓸까? j는 0 1 ... m-1 ()
    for i in range(idxi, n):
        if i == idxi:
            for j in range(idxj, m-1): # 처음에는 idxj로 가고 그 다음 i부터는 0부터 다시 시작해야함. -> i가 idxi면 idxj부터. elif i != idxi면 0부터
                # 현재꺼의 왼쪽 오른쪽을 보기
                if sadari[i][j][1] != 1: # 오른쪽에 사다리가 없다면
                    # 그 왼쪽꺼도, 오른쪽꺼도 확인해야함.
                    # 만약 j가 0이라면 j+1만(1)
                    if j == 0:
                        if sadari[i][j+1][1] != 1:
                            # print("사다리 만듦", i, j, "에서 오른쪽으로", curCnt, wantCnt)
                            llist.append((i,j))
                            sadari[i][j][1] = 1 # 사다리 오른쪽 연결
                            sadari[i][j+1][0] = 1 # 사다리 왼:쪽 연결
                            make_sadari(curCnt+1, wantCnt, i, j+2)
                            llist.pop()

                            sadari[i][j][1] = 0
                            sadari[i][j+1][0] = 0
                    # 만약 j가 m-2라면 
                    elif j == m-2:
                        if sadari[i][j][0] != 1: # 왼쪽에 사다리가 없다면
                            # print("사다리 만듦", i, j, "에서 오른쪽으로", curCnt, wantCnt)
                            llist.append((i,j))
                            sadari[i][j][1] = 1
                            sadari[i][j+1][0] = 1
                            make_sadari(curCnt+1, wantCnt, i+1, 0)
                            llist.pop()

                            sadari[i][j][1] = 0
                            sadari[i][j+1][0] = 0
                    # 만약 j가 1~m-3 이라면
                    else:
                        if sadari[i][j][0] != 1 and sadari[i][j+1][1] != 1:
                            # 왼쪽에도 없고 그 너머 오른쪽에도 없다면
                            # print("사다리 만듦", i, j, "에서 오른쪽으로", curCnt, wantCnt)
                            llist.append((i,j))
                            sadari[i][j][1] = 1
                            sadari[i][j+1][0] = 1
                            make_sadari(curCnt+1, wantCnt, i, j+2)
                            llist.pop()

                            sadari[i][j][1] = 0
                            sadari[i][j+1][0] = 0
        else:
            for j in range(0, m-1): 
                # 현재꺼의 왼쪽 오른쪽을 보기
                if sadari[i][j][1] != 1: # 오른쪽에 사다리가 없다면
                    # 그 왼쪽꺼도, 오른쪽꺼도 확인해야함.
                    # 만약 j가 0이라면 j+1만(1)
                    if j == 0:
                        if sadari[i][j+1][1] != 1:
                            # print("사다리 만듦", i, j, "에서 오른쪽으로", curCnt, wantCnt)
                            llist.append((i,j))
                            sadari[i][j][1] = 1 # 사다리 오른쪽 연결
                            sadari[i][j+1][0] = 1 # 사다리 왼:쪽 연결
                            make_sadari(curCnt+1, wantCnt, i, j+2)
                            llist.pop()
                            sadari[i][j][1] = 0
                            sadari[i][j+1][0] = 0
                    # 만약 j가 m-2라면 
                    elif j == m-2:
                        if sadari[i][j][0] != 1: # 왼쪽에 사다리가 없다면
                            # print("사다리 만듦", i, j, "에서 오른쪽으로", curCnt, wantCnt)
                            llist.append((i,j))
                            sadari[i][j][1] = 1
                            sadari[i][j+1][0] = 1
                            make_sadari(curCnt+1, wantCnt, i+1, 0)
                            llist.pop()
                            sadari[i][j][1] = 0
                            sadari[i][j+1][0] = 0
                    # 만약 j가 1~m-3 이라면
                    else:
                        if sadari[i][j][0] != 1 and sadari[i][j+1][1] != 1:
                            # 왼쪽에도 없고 그 너머 오른쪽에도 없다면
                            # print("사다리 만듦", i, j, "에서 오른쪽으로", curCnt, wantCnt)
                            llist.append((i,j))
                            sadari[i][j][1] = 1
                            sadari[i][j+1][0] = 1
                            make_sadari(curCnt+1, wantCnt, i, j+2)
                            llist.pop()
                            sadari[i][j][1] = 0
                            sadari[i][j+1][0] = 0


make_sadari(0, 0, 0, 0)
make_sadari(0, 1, 0, 0)
make_sadari(0, 2, 0, 0)
make_sadari(0, 3, 0, 0)

print(res if res != 100 else -1)
