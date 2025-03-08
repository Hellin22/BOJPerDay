import sys
import heapq
inp = sys.stdin.readline

n = int(inp().strip())
hq = []
cur = 0
for _ in range(n):
    row = list(map(int, inp().strip().split()))
    minn = min(row)
    for i in row:
        heapq.heappush(hq, i)
    
    while True:
        if not hq: break

        if hq[0] <= minn:
            cur+=1
            if cur == n*n-n+1:
                print(hq[0])
                exit(0)
            
            a = heapq.heappop(hq)
        else: break

while hq:
    cur+=1
    if cur == n*n-n+1:
        print(hq[0])
        exit(0)
    heapq.heappop(hq)