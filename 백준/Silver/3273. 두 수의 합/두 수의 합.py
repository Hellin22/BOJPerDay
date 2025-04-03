n = int(input().strip())
llist = list(map(int, input().strip().split()))
wantNum = int(input().strip())
llist.sort()
idx = 0
ans = 0
if n == 0: 
    print(0)
    exit()
dt = dict()
for i in range(n):
    dt[llist[i]] = dt.get(llist[i], 0) + 1

ans = 0
for i in range(n):
    ans += dt.get(wantNum - llist[i], 0)
    if llist[i] == wantNum-llist[i]:
        ans-=1
print(ans//2)