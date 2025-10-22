import sys
inp = sys.stdin.readline

hx, hy, walk, run = map(int, inp().strip().split())
cx, cy = 0, 0
ans = 0
# (0, 0) -> (hx, hy)
# walk가 run보다 큰 경우도 있을수 있음...
# 가까워지는 방향이 뭔지 확인.

# 1. |hx-cx| or |hy-cy| 중에서 작은거만큼 대각선 이동 (2*walk or run) 중에서 작은걸로
# 2. 한칸씩 가야하는데 대각선으로 가는게 더 빠른지 아닌지 확인

# 1. 대각선 이동
# hx, hy는 음이 아닌 정수
if hx >= hy:
    ans += min(2*walk, run) * hy
    cx, cy = hy, hy
else:
    ans += min(2*walk, run) * hx
    cx, cy = hx, hx
# hy == cy -> cx를 바꾸면 됨
diff = -1
if hy == cy:
    diff = hx - cx
else:
    diff = hy-cy
if diff % 2 == 0: # 2로 나눠짐. -> 마지막에 walk 안해도 됨
    ans += min(run, walk) * diff
else:
    ans += min(run*(diff-1)+walk, walk*diff)

print(ans)