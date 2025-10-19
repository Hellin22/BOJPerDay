import sys
from collections import Counter
inp = sys.stdin.readline

# 오른쪽에 있으면서 수열에 등장한 횟수가 더 많은 것.

n = int(inp().strip())
llist = list(map(int, inp().strip().split()))
ct = Counter(llist)

# 1. 등장횟수가 더 많으면 
# 애초에 저장할게 (등장횟수, 실제 숫자, idx) -> 이렇게 저장하면 될거같네

stck = []
answer = [-1] * n
for i in range(n):
    while stck and stck[-1][0] < ct[llist[i]]: # 나의 등장횟수가 더 크다면 -> 3 3 3 ... 4가 나오면 3을 모두 빼주기
        cnt, num, idx = stck.pop()
        answer[idx] = llist[i]
    stck.append((ct[llist[i]], llist[i], i))
print(' '.join(map(str, answer)))