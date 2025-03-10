import sys
inp = sys.stdin.readline

n, s = map(int, inp().strip().split())
llist = list(map(int, inp().strip().split()))

le = 0
ri = 0
cur_len = ri-le+1
cur_sum = llist[ri]
res = 100001
while True:
    if cur_sum >= s:
        # print(le, ri, res, cur_sum, cur_len)
        res = min(res, cur_len)
        if le == ri:
            ri +=1
            if ri == len(llist):
                break
            cur_sum+=llist[ri]
            cur_len+=1
        elif le < ri:
            cur_sum -= llist[le]
            le +=1
            cur_len-=1
    elif cur_sum < s:
        ri+=1
        if ri == len(llist): # 종료해야함. 밑에서 다시
            break
        cur_len+=1
        cur_sum+=llist[ri]

# 이제 ri는 끝에 다다랏고
# le는 끝이나 그전에 옴.

while True:
    if cur_sum >= s:
        res = min(res, cur_len)
        cur_sum-= llist[le]
        le+=1
        cur_len-=1

    if cur_sum < s:
        break
    if le > ri or le == len(llist): break


print(res if res != 100001 else 0)