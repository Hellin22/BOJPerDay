from collections import deque
from copy import deepcopy
N, M, R = map(int, input().strip().split())

arr = [list(map(int, input().strip().split())) for _ in range(N)]

# 반시계 방향으로 R 회전 -> dq.rotate(-R)
# 만약 껍데기 순서에 따라 이거 구분해라
# -> i %2가 0이면 시계 아니면 반시계로 (R)을 먼저 구하고 이거에 따라서 for문 다르게

new_arr = deepcopy(arr)

loops = min(N, M) // 2
for i in range(loops):
    dq = deque()

    # arr[0][0~M-1]
    # arr[1][1~M-2]
    dq.extend(arr[i][i:M-i]) # 제일 위에꺼 추가하기

    # 오른쪽꺼 더하기
    # arr[1][M-1]    arr[2][M-1-1]
    # arr[2][M-1]    arr[3][M-1-1]
    # ...                2칸 위라는거임
    # arr[N-1-1][M-1]   arr[N-1-1-1][M-1-1]
    # arr[N-1-i][M-1] 이거 앞까지 진행

    # arr[i+1][M-1] ~ arr[N-1-1][M-1]
    # row[M-1-i] for row in arr[i+1:N-1-i]

    # arr[i-1][M-1-i]에서

    dq.extend(row[M-1-i] for row in arr[i+1:N-1-i])


    # 거꾸로 하는거임. 나중에 뒤집으면 되니까 마지막꺼 생각
    # arr[N-1][0~M-1]
    # arr[N-1-1][1~M-1-1]
    #
    # arr[0~M-1][N-1]
    # arr[1~M-1-1][N-1-1]
    # y는 M-1 고정
    # y는 M-1-i
    # arr[i:M-1-i][N-1-i]
    dq.extend(arr[N-1-i][i:M-1+1-i][::-1])

    # 위에꺼부터 가져오면 되겟지? x가 바뀜.
    # x가 어디부터 어디까지인지 설정 후 그걸 col로 for하면 됨
    # arr[0][1] arr[1][1] ... arr[N-1-1][1]
    # arr[1][2] arr[2][2] /... arr[N-1-2][2]
    #
    # row는 i~N-1-i까지
    dq.extend([row[i] for row in arr[i+1:N-1-i]][::-1])
    #
    # arr

#     dq.extend([row[i] for row in arr[i+1: N-i-1]][::-1])


    dq.rotate(-R)

    # 위 껍데기 x좌표는 0 1 ... i로 고정
    # y좌표는 0~M-1, 1~M-2 i에서 M-1-i까지
    for j in range(i, M-i):
        new_arr[i][j] = dq.popleft()
#     # 상(위껍데기)
#     for j in range(i, M-i):
#         new_arr[i][j] = dq.popleft()


    # 오른쪽은 y좌표가 m-1이다가 m-1-1이다가 -> m-1-i
    # x좌표는 1~n-1-1, 2~n-1-1-1
    for j in range(i+1, N-1-i-1+1):
        new_arr[j][M-1-i] = dq.popleft()

#
#     # 우(오른쪽 껍데기 1번째부터 시작함.)
#     for j in range(i+1, N-i-1):
#         new_arr[j][M-i-1] = dq.popleft()
#




    # 아래쪽을 추가해야함.
    # x가 고정임. N-1, N-1-1, N-1-2 ... 즉, X는 N-1-I
    # y는? 일단 반대로 해야함.
    # m-1 ... 0 / m-2 ... 1 -> 시작은 m-1-i, 0+i-1, -1
    for j in range(M-1-i, i-1, -1):
        new_arr[N-1-i][j] = dq.popleft()

#     for j in range(M-1-i, -1+i, -1):
#         new_arr[N-1-i][j] = dq.popleft()
#



    # 왼쪽꺼를 채워야함.
    # y가 고정 -> 0, 1, 2, ... -> i임.
    # 반대로 해야함.
    # N-2 ~ 1 / N-3 ~ 2 / N-1-1-i, i+1-1, -1
    for j in range(N-1-1-i, i, -1):
        new_arr[j][i] = dq.popleft()
#     for j in range(N-i-2, i, -1):
#         new_arr[j][i] = dq.popleft()

for i in range(len(new_arr)):
    print(*new_arr[i])