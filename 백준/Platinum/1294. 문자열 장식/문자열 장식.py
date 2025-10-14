from heapq import heappush, heappop
import sys
inp = sys.stdin.readline

n = int(inp().strip())
llist = [[] for _ in range(n)]
for i in range(n):
    llist[i] = list(inp().strip())[::-1]

sttr = ""

while llist:

    cur = "z"
    group = []

    for i in range(len(llist)):
        if llist[i][-1] < cur: # 더 작은 문자를 발견했다면
            cur = llist[i][-1]
            group = [i]
        elif llist[i][-1] == cur: # 같은 문자라면
            group.append(i)

    # group이 비어있을 수는 없음.

    # 이제 group을 모두 돌면서 비교
    group_idx = -1
    for i in range(len(group)):
        # 뭐랑 뭐를 비교해야하지?
        # group = [1, 2, 3, 4, 5] -> group[i]는 llist의 idx를 의미.
        group[i] = (''.join(llist[group[i]][::-1]), group[i]) # tmp_str은 llist[i]번의 str을 다시 원상태로 복구한것
    
    group.sort() # str 사전순으로 정렬

    # group에서 같은걸 포함하는 경우 문제
    # -> 어떻게 처리할 것인가?
    # 2개의 string을 모두 합쳐서 처리?
    # 끝에서 부터 2개 꺼내서 -> 종료조건은 group이 1개 남을때까지

    while len(group) > 1:
        hq = []
        fir, sec = group.pop(), group.pop()

        heappush(hq, (fir[0]+sec[0], fir[1]))
        heappush(hq, (sec[0]+fir[0], sec[1]))

        if hq[0][1] == fir[1]:
            group.append(fir)
        else:
            group.append(sec)


    # group[0]번째꺼를 처리하면 됨.
    sttr += llist[group[0][1]].pop()
    
    if not llist[group[0][1]]:
        llist.pop(group[0][1])


print(sttr)


# xxxba xxxxab
# 결국에 왼쪽꺼부터 처리해야함.
# xxxba xxxxab

# DBAC DBACA 