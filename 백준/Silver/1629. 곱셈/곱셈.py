import sys
inp = sys.stdin.readline


a, b, c = map(int, inp().strip().split())
llist = []
while b != 1:
    if b % 2 == 1: # 홀수인 경우
        b-=1
        llist.append(1)
    else: llist.append(0)
    b//=2

res = a%c
for gob_2 in range(len(llist)-1, -1, -1):
    res = (res*res)%c
    if llist[gob_2] == 1: # a를 곱해주기
        res = (res*a)%c

print(res)