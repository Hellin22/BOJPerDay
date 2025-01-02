import sys
import heapq

inp = sys.stdin.readline

pq = []
llist = []
n = int(inp().strip())
visit = [0] * n # visit가 0이면 방문x -> 폭약이 존재한다는것
res = []

for i in range(n):
    pi = int(inp().strip())
    llist.append(pi)
    heapq.heappush(pq, (-pi, -i))

while pq:
    # pq가 비어있지 않다면 
    # pq에서 값을 하나 빼고 + 그 값을 기준으로 visit 배열을 살펴보면서 터지는지 안터지는지 확인
    cur, curidx = heapq.heappop(pq) # 폭약 최대값, 그때의 idx
    cur, curidx = -cur, -curidx
    if visit[curidx] == 1: continue # 이미 폭약 터진자리면 아무것도 안함
    visit[curidx] = 1 # 폭약 터뜨리기
    # curidx+1 ~ n-1, curidx-1 ~ 0까지 폭약 터뜨릴 수 있으면 터뜨리기
    if(curidx + 1 < n):
        next = cur
        nextidx = curidx
        for i in range(nextidx+1, n, 1):
            # 폭약이 안터졌다면 터질수 있는지 보고 반복
            if(visit[i] == 1): break # 이미 터져있으므로 종료하기
            if(llist[i] >= next): break # 폭약이 터질 수 없음.
            else: # 폭약이 터질 수 있음
                next = llist[i]  # 다음 폭약 데미지는 next임
                visit[i] = 1 # 폭약 터졌으니까 1로 바꾸기
    
    if(curidx - 1 >= 0):
        prev = cur
        previdx = curidx
        for i in range(previdx-1, -1, -1):
            if(visit[i] == 1): break
            if(llist[i] >= prev): break
            else :
                prev = llist[i]
                visit[i] = 1
    res.append(curidx + 1)
res.sort()
for i in res:
    print(i)