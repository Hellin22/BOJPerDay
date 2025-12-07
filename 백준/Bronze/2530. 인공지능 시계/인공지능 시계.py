h, m, s = map(int, input().split())
add = int(input())

# 전체 초 계산
total = h * 3600 + m * 60 + s + add

# 시, 분, 초 계산
h = (total // 3600) % 24
m = (total % 3600) // 60
s = total % 60

print(h, m, s)
