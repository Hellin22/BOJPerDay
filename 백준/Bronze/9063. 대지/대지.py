import sys
input = sys.stdin.readline

N = int(input().strip())

# 초기값 — 문제 제약 내 좌표 범위 고려
min_x = 10000
max_x = -10000
min_y = 10000
max_y = -10000

for _ in range(N):
    x, y = map(int, input().split())
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

width = max_x - min_x
height = max_y - min_y
print(width * height)
