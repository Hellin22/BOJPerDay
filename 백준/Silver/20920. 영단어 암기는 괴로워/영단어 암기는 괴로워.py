import sys
inp = sys.stdin.readline

n, m = map(int, inp().strip().split())

# m보다 짧으면 안외움
dict = {}
for i in range(n):
    sttr = inp().strip()
    if len(sttr) < m: continue
    dict[sttr] = dict.get(sttr, 0) + 1

# 자주 + 긴거 + 사전순
# cnt(x), -len(x), x

llist = sorted(dict, key=lambda x: (-dict[x], -len(x), x))

print(' '.join(llist))