import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    # 층 계산 (y)
    floor = N % H
    # 호 계산 (x)
    room = N // H + 1

    # 만약 나머지가 0이면 꼭대기 층
    if floor == 0:
        floor = H
        room -= 1

    # 방 번호는 층 * 100 + 호
    print(floor * 100 + room)
