from collections import deque
import sys
inp = sys.stdin.readline

n, w, limitt = map(int, inp().strip().split(" "))
curWeight, curIdx, res = 0, 0, 0
q = deque()
llist = list(map(int, inp().strip().split()))

while(curIdx != len(llist)):
    if len(q) == w:
        curWeight -= q.popleft()

    weight = 0
    if(curWeight+llist[curIdx]<=limitt):
        q.append(llist[curIdx])
        weight=llist[curIdx]
        curIdx+=1
    else: 
        q.append(0)

    curWeight+=weight
    res += 1
print(res + max(w, len(q)))