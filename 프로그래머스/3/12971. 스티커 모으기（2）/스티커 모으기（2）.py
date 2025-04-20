'''
최대한 많이 떼어낼 수 있음.
-> 이때, 한번 떼어낸다? 그러면 양옆에꺼는 못떼어냄
길이는 n인데 1~100,000

어떤거를 떼어내겠다. -> a[i], a[i-1] + a[i+1] a[i]가 더 클때만 떼어낼까?

14 5 3 2
6 11 9 10

1 3 2 5 4
3 5
1 2
2 4

1 3 2 4 5

3 5임
'''


def solution(sticker):
    answer = 0
    maxx = -1
    n = len(sticker)
    arr = [[0] * n for _ in range(2)]
    # 0. 길이가 1인 경우 -> 예외처리 해주기
    if n == 1:
        return sticker[0]
    
    # 1. 첫번째꺼를 선택안할 경우
    for i in range(1, n):
        arr[0][i] = max(arr[0][i-1], arr[0][(i-2) % n], arr[1][(i-2) % n])
        arr[1][i] = max(arr[0][i-1], arr[1][(i-2)%n]) + sticker[i]
    maxx = max(max(row) for row in arr)
    
    # 2. 선택 o -> 마지막, 왼쪽은 선택 불가능
    arr = [[0] * n for _ in range(2)]
    for i in range(0, n-1):
        if i == 1: continue # 1번도 못뜯음
        arr[0][i] = max(arr[0][i-1], arr[0][(i-2) % n], arr[1][(i-2) % n])
        arr[1][i] = max(arr[0][i-1], arr[1][(i-2)%n]) + sticker[i]
    
    maxx = max(maxx, max(max(row) for row in arr))

    return maxx