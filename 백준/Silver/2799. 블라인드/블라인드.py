import sys
inp = sys.stdin.readline

n, m = map(int, inp().strip().split())

llist = [inp().strip() for _ in range(n*5+1)]

res = [0, 0, 0, 0, 0]
for i in range(n):
    for j in range(m):
        st_cnt = 0
        for k in range(4):
            if llist[i*5 +1+k][j*5 +1] == "*":
                st_cnt+=1
            else:
                break
        res[st_cnt]+=1

print(*res)