import sys

inp = sys.stdin.readline

# 오른쪽에 있으면서 a보다 큰 수 중 가장 왼쪽에 있는 수
# 3 5 2 7 -> 5 7 7 -1

n = int(inp().strip())
llist = list(map(int, inp().strip().split()))
stck = []
# stck이 비어있다면 추가
# stck이 안비어있다면 증가하는걸 유지한채로 추가
# 만약 stck[-1]보다 현재값이 크면 그 값은 현재 값
# stck에는 [num, idx] 추가

answer = [-1] * n
for i in range(n):
    cur = llist[i]
    if not stck:
        stck.append((cur, i))
    else:
        while stck and stck[-1][0] < cur:
            # 현재값이 더 크다면 이전꺼는 뺌.
            answer[stck.pop()[1]] = cur
        stck.append((cur, i))

print(' '.join(map(str, answer)))