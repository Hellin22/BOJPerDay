import sys

inp = sys.stdin.readline

acnt, bcnt = map(int, inp().strip().split())
alist = set(map(int, inp().strip().split()))
blist = set(map(int, inp().strip().split()))
print(len(alist-blist) + len(blist-alist))