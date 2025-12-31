import sys

input = sys.stdin.readline

M = int(input().strip())
N = int(input().strip())

total = 0
min_val = None

i = 1
while i * i <= N:
    sq = i * i
    if M <= sq <= N:
        total += sq
        if min_val is None:
            min_val = sq
    i += 1

if min_val is None:
    print(-1)
else:
    print(total)
    print(min_val)
