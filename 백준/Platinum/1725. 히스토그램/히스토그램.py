import sys
inp = sys.stdin.readline

stck = []
# 1. stck에는 idx 저장
# 2. stck의 데이터는 항상 오름차순으로 유지
# 3. if not stck -> push
# 4. else: llist[stck의 top]과 현재 llist[idx]를 비교해서 높이가 낮아진다? 그러면 그때부터 계산
# 5. while llist[stck.top] > llist[idx]
# 6. 현재 idx가 오른쪽을 담당하고 stck.top이 왼쪽 좌표 -> idx - stck.top - 1 = 밑변의 길이
# 7. 높이 = llist[stck.top]
# 8. 이걸 계속 갱신
# 9. 마지막에는 어떻게 하는가? -> stck에 idx가 남아있다면? == 이전과 똑같은 방식으로 밑변 바꾸면서 높이는 llist[stck.top]

n = int(inp().strip())
llist = []
for _ in range(n):
    llist.append(int(inp().strip()))

answer = 0
stck = []
for i in range(n):
    if not stck: # stck이 비어있다면 push
        stck.append(i) # idx 추가
    else:
        while stck and llist[stck[-1]] > llist[i]: # 감소되는게 들어온다면? 그때부터 계싼
            # 동일한건 괜찮음
            height = llist[stck.pop()]
            if stck:
                under = i - stck[-1]-1
            else:
                under = i
            answer = max(answer, height * under)
        stck.append(i) # idx 추가

while stck:
    height = llist[stck.pop()]
    if stck:
        under = n - stck[-1]-1
    else:
        under = n
    answer = max(answer, height * under)

print(answer)
