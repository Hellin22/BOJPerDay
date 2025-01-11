from collections import deque
import sys
inp = sys.stdin.readline

n, w, limitt = map(int, inp().strip().split(" "))
# 전체 트럭 개수, 다리 트럭 올 수 있는 개수, 다리 최대 하중
curWeight = 0
curCnt = 0
curIdx = 0
finishIdx = 0
res = 0
q = deque()
llist = list(map(int, inp().strip().split()))

# 초기 세팅
# 
while(len(q) != w):
    if(curIdx == len(llist)): 
        print(res + w)
        exit()
    # 트럭이 올 수 있음
    if(curWeight + llist[curIdx] <= limitt):
        q.append(llist[curIdx])
        curWeight+=llist[curIdx]
        curIdx+=1
    else:
        q.append(0)
    res+=1

while(curIdx != len(llist)):
    # 1. 하나 빼내기
    appendNumber = q.popleft()
    curWeight-=appendNumber

    # 2. 하나 추가하기
    if curWeight + llist[curIdx] <= limitt:
        q.append(llist[curIdx])
        curWeight+=llist[curIdx]
        curIdx+=1
    else: q.append(0)
    res+=1

print(res+len(q))