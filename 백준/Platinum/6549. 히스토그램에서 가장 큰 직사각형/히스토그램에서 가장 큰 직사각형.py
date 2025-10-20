import sys
inp = sys.stdin.readline

# 1. stck에는 idx 저장
# 2. stck의 데이터는 항상 오름차순으로 유지
# 3. if not stck -> push
# 4. else: llist[stck의 top]과 현재 llist[idx]를 비교해서 높이가 낮아진다? 그러면 그때부터 계산
# 5. while llist[stck.top] > llist[idx]
# 6. 현재 idx가 오른쪽을 담당하고 stck.top이 왼쪽 좌표 -> idx - stck.top - 1 = 밑변의 길이
# 7. 높이 = llist[stck.top]
# 8. 이걸 계속 갱신
# 9. 마지막에는 어떻게 하는가? -> stck에 idx가 남아있다면? == 이전과 똑같은 방식으로 밑변 바꾸면서 높이는 llist[stck.top]
while True:
    llist = list(map(int, inp().strip().split()))
    n = llist[0]
    if llist[0] == 0: break
    llist = llist[1:]
    stck = []

    answer = 0
    stck = []
    for i in range(n):
        # 스택이 비었거나 현재 높이가 크거나 같으면 push
        while stck and llist[stck[-1]] > llist[i]:
            height = llist[stck.pop()]
            if not stck:
                width = i
            else:
                width = i - stck[-1] - 1
            answer = max(answer, height * width)
        stck.append(i)

    while stck:
        height = llist[stck.pop()]
        if stck:
            under = n - stck[-1]-1
        else:
            under = n
        answer = max(answer, height * under)

    print(answer)
