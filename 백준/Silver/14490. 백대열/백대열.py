import sys

inp = sys.stdin.readline

n, m = map(int, inp().strip().split(":"))
nreal, mreal = n, m
gcd = 0
swapFlag = False
if(m > n):
    n, m = m, n

while (m != 0):
    # gcd(n, m) = gcd(m, n%m)
    nModem = n%m
    n, m = m, nModem

# m이 0이라면
gcd = n
nreal, mreal = nreal / gcd, mreal / gcd

print(''.join(map(str, [int(nreal), ":", int(mreal)])))