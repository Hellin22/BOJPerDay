import sys
from collections import deque
inp = sys.stdin.readline


# n명의 사람들의 키가 주어짐

n = int(inp().strip())
llist2 = []
for i in range(n):
    a = int(inp().strip())
    llist2.append(a)

# 처음부터 같은 숫자 축약해버리기
llist = []
i = 0
while i < len(llist2):
    cur = i
    while cur < len(llist2):
        if llist2[cur] != llist2[i]: break
        cur+=1
    # cur-1 ~ i +1이 개수
    llist.append([llist2[i], cur-1-i+1])
    i = cur
stck = []

# stck에는 (숫자, 숫자의 개수) append
# stck은 항상 내림차순으로 정렬 할 예정
# 만약 이전보다 큰 값이 들어오면 stck이 내림차순 될때까지 빼야함.
# 이때 뺄때의 조건이 중요
# 1. 하나를 빼고나서 stck이 빈다. -> n*n+1/2
# 2. 하나를 빼고나서 stck이 안빈다. -> n+1 * n+2 / 2
# 3. 더 작은 값이면 그냥 넣기
# 다 넣고나서 stck이라면 -> pop 하면서 n*n+1/2
ans = 0
for wonso, wonso_cnt in llist:
    # stck에는 (값, 개수)
    # 비어있는 경우 -> 제일 처음밖에 없음. -> 추가
    if not stck: stck.append([wonso, wonso_cnt])

    # 비어있지 않은 경우 -> 내림차순을 유지해야함.
    else:
        cur, cur_cnt = wonso, wonso_cnt
        prev, prev_cnt = stck[-1]

        # 1. 만약 현재 값이 더 작다면 그냥 추가
        if cur < prev:
            stck.append([cur, cur_cnt])
        # 2. 현재 값하고 똑같다면 개수 하나 증가
        elif cur == prev:
            stck[-1][1] += cur_cnt
        # 3. 현재 값보다 더 크다면 내림차순 만족할때까지 stck.pop 진행 -> ans 바뀜
        else:
            while stck and stck[-1][0] < cur:
                # stck[-1][0]가 같은 경우도 고려해주기


                prev, prev_cnt = stck.pop()
                # 1. prev가 빠질 때 그 이전거랑 매칭되는 경우
                if stck: # stck이 남아있으면 그거랑 prev랑 매칭되는거 ans 추가
                    ans += (prev_cnt) * (prev_cnt+1) // 2
                    ans -= (prev_cnt-1) * prev_cnt // 2 # 중복 처리되는거 없앰
                
                # 2. prev랑 cur랑 매칭되는거 추가
                ans += (prev_cnt) * (prev_cnt+1)//2

                # prev랑 하나로 묶어서 처리하면 안될거같음..
                # 즉, pprev, prev, cur 이렇게 있을 때
                # pprev랑 prev + prev랑 cur 이렇게 처리해야할거같음.

                # 1. if stck -> prev_cnt만큼 추가
                # 2. if not stck -> 안함.
                # 3. prev_cnt랑 cur이랑 비교해서 추가

                

            # 다 뺐다면 stck이 비어있는지 or stck[-1][0]가 cur인지 확인
            if stck and stck[-1][0] == cur:
                stck[-1][1] += cur_cnt
            else:
                stck.append([cur, cur_cnt])
# 다 끝난 후에 stck에 원소가 있다면 -> 그거에 대해서 처리
stck = deque(stck)
while stck:
    if len(stck) >= 2:
        ans += stck[-1][1] + stck[-1][1] * (stck[-1][1]-1) //2
    else: # 하나만 있음
        ans += stck[-1][1] * (stck[0][1]-1) //2

    stck.pop()
print(ans)
