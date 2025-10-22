import sys
inp = sys.stdin.readline

hx, hy, walk, run = map(int, inp().strip().split())
cx, cy = 0, 0
ans = 0
diff = -1
if hx >= hy:
    ans += min(2*walk, run) * hy
    diff = hx-hy
else:
    ans += min(2*walk, run) * hx
    diff = hy-hx
if diff % 2 == 0:
    ans += min(run, walk) * diff
else:
    ans += min(run*(diff-1)+walk, walk*diff)

print(ans)