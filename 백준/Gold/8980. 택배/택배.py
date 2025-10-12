from heapq import heappush, heappop
from collections import defaultdict
import sys
inp = sys.stdin.readline

'''
보내는 마을 -> 받는 마을 -> 박스 개수

트런은 총 용량이 존재함.

보내는 마을 -> 받는 마을이 가까울 수록 


박스 보내는 마을 < 받는 마을 -> 이거 중요

아 최대 개수를 측정해야하네?


보내는 마을, 받는 마을을 오름차순 정렬해서 (도착지점, 택배 개수) 이렇게 저장?
minheap 사용

if 2번에 도착했다.

-> 예시 들어봄
(1, 5, 45), (2, 3, 20), (2, 4, 20), (3, 4, 30)
이렇게 있으면 5번에 넣어야 하지만 3, 4로 처리하면 더 많이 가능함.

그러면 일단 담아야 할듯?
minheap하고 전체 담겨있는 택배 개수도 유지할 필요가 있음.
즉, all_cnt = 0, cnt_jehan = 40

만약 all_cnt가 cnt_jehan보다 작다?
all_cnt가 cnt_jehan을 안넘게 담기

minheap.push(5, 40) -> 도착지(5), 택배수(40)

2번으로 감. -> 2번에 뺄게 있는지? 즉, minheap and minheap[0][0]가 2인지 확인
계속 빼고 ans에 추가
뺄때마다 all_cnt 마이너스 해주기

만약 다 했고 2번에서 택배 추가할게 있다?
그러면 추가할 수 있는거. 즉, 2번에서 보내는거를 모두 가져옴.
all_cnt가 cnt_jehan을 안넘을때까지 넣어야함.
그런데 그 전에 얼마나 많이 넣을 수 있는지 확인해야함.
즉, 지금 5, 40이 있는데 2, 20 / 3, 20을 하면 더 빨리 되기 때문에 5, 40을 빼야함.
만약 2, 20 / 3, 15라면? 5. 40을 빼지만 5, 5를 넣을 수 있음. 이거 예외처리 해주기


'''

maxhq = []
all_cnt = 0

n, cnt_jehan = map(int, inp().strip().split())
arr = [[] for _ in range(n+1)]
ans = 0
m = int(inp().strip())
for _ in range(m):
    a, b, c = map(int, inp().strip().split())
    arr[a].append((b, c)) # 도착지, 택배 수

for i in range(1, n+1):
    arr[i].sort() # 오름차순 정렬 -> 택배 수는 상관업승ㅁ

dt = defaultdict(int)

for i in range(1, n+1):
    # 모든 마을에 대해서 돌면서

    # print(f"현재 마을 번호는 {i}번째 마을 입니다.")
    # print(f"현재 dt와 heap은 {dt}{maxhq}, 현재 무게는 {all_cnt}")

    # 1. 해당 마을 arr[i]에 내릴 택배가 있다면?
    if i in dt: # i라는 마을이 dt 안에 있다면
        # print(dt)
        ans += dt[i] # 정답
        all_cnt -= dt[i] # 전체 개수

        del dt[i] # 모두 다 썻으니까 삭제

    # print(f"{i}번째 마을에서 택배 다 내린 후의 dt = {dt}")

    # 2. 해당 마을 arr[i]에서 추가할 수 있다면? -> 도착지가 가장 먼거를 없애야함.
    for dest, cnt in arr[i]: 
        # (dest, cnt)가 오름차순 정렬되어 저장되어있음
        # 이걸 모두 저장하고 all_cnt가 cnt_jehan 넘는다? 그러면 max_heap에서 빼주기
        heappush(maxhq, (-dest, cnt))
        dt[dest] += cnt
        all_cnt += cnt

    # print(f"{i}번째 마을에서 택배 다 추가하고 dt와 hq, 무게는: {dt, maxhq, all_cnt}")


    # 3. all_cnt가 cnt_jehan을 넘는다면 maxhq에서 빼서 cnt_jehan을 안넘게 맞추기
    while all_cnt > cnt_jehan:
        dest, cnt = heappop(maxhq)
        dest = -dest
        dt[dest] -= cnt
        all_cnt -= cnt

        # 35 40
        if all_cnt < cnt_jehan: # all_cnt에서 cnt를 뺐을 때 cnt_jehan을 안넘는다면
            # ==인 경우에는 다시 추가 안해줘도 되기 때문
            heappush(maxhq, (-dest, cnt_jehan - all_cnt))
            dt[dest] += cnt_jehan - all_cnt
            all_cnt = cnt_jehan

    # print(f"무게 맞추고 나서는 어떻게 되는가? {dt, maxhq, all_cnt}")
    # print()

print(ans)
    
