import sys
inp = sys.stdin.readline

n, m = map(int, inp().strip().split())

llist = [0] * n
for i in range(n):
    llist[i] = int(inp().strip())

llist.sort()

le, ri = 0,0
res = sys.maxsize
if m == 0:
    print(0)
    exit(0)

while True:
    # 1. llist[ri] - llist[le]가 m 이상 이라면?
    if llist[ri] - llist[le] >= m: # res 갱신 가능
        res = min(res, llist[ri] - llist[le])
        le+=1
    
    # 2.
    elif llist[ri] - llist[le] < m: # res 갱신 불가능
        ri+=1 # ri를 늘려서 해당값 안에 들어가게하기
    
    if ri == len(llist):
        break # ri가 인덱스 범위를 벗어나면 종료

    # m이 0인 경우는 어떻게 고려? -> 따로 예외처리
    # m이 1 이상인 경우에는 오름차순으로 했기 때문에 le가 더 커지는 경우는 없음

for i in range(n-1, le-1, -1):
    if llist[n-1] - llist[i] >= m:
        res = min(res, llist[n-1] - llist[i])
        break
print(res)
