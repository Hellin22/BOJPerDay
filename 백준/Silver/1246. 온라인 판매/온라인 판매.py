import sys 
inp = sys.stdin.readline

# n명이 있고 m개의 가격이 있고 각각 1000개가 있음. -> 파이썬은 약 2천만을 타겟으로 잡으면 된다고함... -> 이게 먼 의미가 있나? nm으로도 충분히 풀릴거같은 문제
# but 더 빠른 풀이법이 존재할거같다고 생각함.-> dp로도 충분히 해결 가능할거같음.
# 달걀은 n개 있지만 m명의 고객에게 팔아야함. -> 달걀 총 수량을 초과해서는 못팜
# m개의 list를 sort해서 list[-1]의 가격부터 시작해서 제일 많은 가격을 가져오면 될듯?
n,m = map(int, inp().strip().split())
list = [int(inp().strip()) for _ in range(m)]

list.sort()
# list는 정렬된 상태로 존재 -> 제일 오른쪽 [-1]이 제일 높은 금액임

# 처음 price는 최대값, summ은 0 -> price는 계속해서 1 낮춘 금액으로 초기화
# -> 1 낮춘걸로 해야하는가? -> 아닌거같음. 그 전껄로 하면 될거같음.
price = list[-1]
summ = 0
curPrice = price
curSum = summ

for i in range (m):
    curPrice = list[i]
    curSum = 0
    curn = n
    for j in range(i, m): # j는 i부터 그 이후까지 진행해야함.
        curSum += curPrice
        curn-=1
        if curn == 0: 
            break

    if(curSum > summ):
        price = curPrice
        summ = curSum

print(price, summ)