import sys

inp = sys.stdin.readline

n = int(inp().strip())
llist = list(map(int, inp().strip().split()))

# 뒤에서부터 보면서 현재값이 이전꺼보다 클때까지 반복

cur_idx = n-1
res = 0
while cur_idx != 0 and cur_idx != -1:
    tmpres = 0
    tmpi = -1
    for i in range(cur_idx-1, -1, -1):
        if llist[cur_idx] >= llist[i]:
            tmpres += llist[i]
        else:
            tmpi = i # i번째에서 불가능한 것
            break
    res-=tmpres
    res+= llist[cur_idx] * (cur_idx-tmpi-1)
    cur_idx = tmpi

print(res)