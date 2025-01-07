import sys

inp = sys.stdin.readline

n, l = map(int, inp().strip().split())
# arr 크기는 1000개로 하기 -> 오른쪽 하나 추가하려고 1로 추가?

waterHoles = list(map(int, inp().strip().split()))

llist = [[1, 1] for _ in range(0, 1002, 1)]
# arr(0)(0) ~ arr(1001)(1)까지 존재.
# arr[i][j]가 0이면 구멍상태, 1이면 정상, 2면 테이프 상태
for i in range(len(waterHoles)):
    llist[waterHoles[i]][0], llist[waterHoles[i]][1] = 0, 0

curi, curj, cnt = 0, 0, 0

# n이 1000이면 l이 1000이면 -> 2000까지 해야하나?
for i in range(0, 1002, 1):
    for j in range(0, 2, 1):
        if(llist[i][j] == 0):
            cnt+=1
            curlength = l * 2 + 1 # j를 0 1로 나눴기 때문
            if(j == 0): 
                if(llist[i-1][1] == 1):
                    llist[i-1][1] = 2
                    curlength -= 1
                    # elif는 테이프 붙어있는 상황밖에 나올 수 없음.
            elif(j == 1):
                if(llist[i][0] == 1):
                    llist[i][0] = 2
                    curlength -=1
            # 만약 구멍이 없다면 넘어가기 -> if문 안에서 구멍이 나왔으니 
            # curlength가 0이 될때까지 진행해야함.
            # 01 10 11 20
            curi, curj = i, j 
            # 0이면 실행 하면 안됨
            for ii in range(curi, 1002, 1):
                if(curlength == 0): break
                for jj in range(curj, 2, 1):
                    llist[ii][jj] = 2 # 테이프 칠하기기
                    curlength-=1
                    if(curlength == 0): break

print(cnt)