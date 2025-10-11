import sys
from heapq import heappush, heappop
inp = sys.stdin.readline

'''
n개의 보석 -> 무게, 가격
k개의 가방 -> 용량 제한

가방에 담을 수 있는 보석 최대가격
가방에는 보석 1개만 담을 수 있음.

n, k
m,v ->n개의 줄
c -> k개의 줄

보석은 무게가 있음.
그 무게를 견디는 가방들 중에서 최소 가격을 가지고 있는 가방과 비교해야함.

(weight, money)

weight, money 순으로 정렬? 오름차순
1 65

무거운거부터 무거운거에 넣기?

hq에 저장할거는? (23, 10) -> 23 가격을 10에 넣은 것. 지금은 가격만 필요하기 때문

무거운거부터 하기 때문에 무조건 가능함.
이렇게 하면 될거같은데?

3 2
1 65
5 23
2 99
10
2
'''

# 1. hq에는 (23, 10) -> 보석 가격, 가방 무게 저장
# 2. 가격, 무게 (가격 높은거, 무게 높은거) 순서로 정렬한거 거꾸로 뒤집고 하나씩 pop하면서 llist가 빌때까지 진행 -> 무게 높은거, 가격 높은거 순서대로 정렬해야함.
# 3. 마지막에는 hq의 가격 합 저장

hq = []
ans = 0

n, k = map(int, inp().strip().split())
w_m_list = []
for _ in range(n):
    weight, money = map(int, inp().strip().split())
    w_m_list.append((weight, money))

bag_list = []
for _ in range(k):
    weight = int(inp().strip())
    bag_list.append(weight)

# 0. bag_list 오름차순 정렬 -> pop
bag_list.sort()

# 1. w_m_list를 (무게 높은거, 가격 높은거) 순서로 정렬
w_m_list.sort(key = lambda x: (-x[0], -x[1]))
w_m_list = w_m_list[::-1] # w_m_list 거꾸로 정렬 -> 뒤에서부터 pop 진행

# 2. w_m_list가 빌때까지 반복
while w_m_list:
    weight, money = w_m_list.pop()
    # print(f"pop된 weight, money =  {weight, money}")

    # 1. bag_list가 있다면 -> 가방에 넣어야함.
    if bag_list:
        if bag_list[-1] >= weight: # 가방에 넣을 수 있다면
            bag_weight = bag_list.pop()
            heappush(hq, (money, bag_weight)) # 보석 가격, 가방 용량
        else: # 가방에 못넣으면?
            # hq[0][0]보다 작은지 비교
            if hq and hq[0][0] < money: # hq의 최소값보다 큰 경우
                _, bag_weight = heappop(hq)
                heappush(hq, (money, bag_weight))
            else: # hq의 최소값보다 큰경우 넣으면 안됨.
                continue # -> 없애도 됨.
    else:
        # bag_list가 없다면 -> hq와 비교해야함.
        if hq and hq[0][0] < money:
            _, bag_weight = heappop(hq)
            heappush(hq, (money, bag_weight))


        # 가방에 못들어간다면?
        # hq의 제일 위에있는거에 들어갈 수 있는지 확인 -> 무조건 가능함.


for a, b in hq:
    ans += a
print(ans)