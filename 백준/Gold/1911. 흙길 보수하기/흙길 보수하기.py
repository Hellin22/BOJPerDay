import sys
inp = sys.stdin.readline

# n과 l -> n은 물웅덩이 개수, l은 널빤지 길이
# 모든 물웅덩이 덮고싶을때 널빤지 최소개수

# n, l
# n개의 웅덩이 정보 -> 시작과 끝
# 각 위치는 0~10억
# 완탐으로는 불가능함.
# 수학을 추가해야할듯

n, l = map(int, inp().strip().split())
llist = []
ans = 0
cur = -1 # 현재 널빤지로 되어있는 오른쪽 좌표
for _ in range(n):
    fromm, to = map(int, inp().strip().split())
    llist.append((fromm, to))
    # 1. fromm이 cur보다 큰경우 -> cur = fromm으로 바꾸고 진행.
    # 2. fromm이 cur보다 작은 경우 -> cur부터 진행.

llist.sort()

for fromm, to in llist:
    if fromm > cur: 
        cur = fromm
    
    # cur에서부터 to까지를 널빤지로 감싼 후에
    # cur 갱신 필요
    # 1 ~ 6이라면 1 2 3 4 5 6 7 -> to-cur+1이 총 길이 -> to-cur+1 // l -> ans 플러스하기
    # cur = to+1
    diff = (to-cur+l-1)//l
    ans += diff
    cur = cur + diff*l

print(ans)

