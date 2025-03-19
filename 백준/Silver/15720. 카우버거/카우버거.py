import sys

inp = sys.stdin.readline

a, b, c = map(int, inp().strip().split())

burger = list(map(int, inp().strip().split()))
side = list(map(int, inp().strip().split()))
beverage = list(map(int, inp().strip().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
beverage.sort(reverse=True)

min_cnt = min(a, b, c)

halin_res = 0
for i in range(min_cnt):
    halin_res+=(burger[i]+side[i]+beverage[i])

res = halin_res
halin_res*=0.9
for i in range(min_cnt, a):
    res+=burger[i]
    halin_res+=burger[i]
for i in range(min_cnt, b):
    res+=side[i]
    halin_res+=side[i]
for i in range(min_cnt, c):
    res+=beverage[i]
    halin_res+=beverage[i]

print(f"{res}\n{int(halin_res)}")