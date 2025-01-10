import sys
inp = sys.stdin.readline

n, m = map(int, inp().strip().split())
llist = [list(map(int, inp().strip().split())) for _ in range(n)]
res = 0

for i in range(len(llist)):
    for j in range(len(llist[i]) - 1):
        res += abs(llist[i][j] - llist[i][j+1])
    res += llist[i][0] + llist[i][-1]

for j in range(m):
    for i in range(n-1):
        res += abs(llist[i][j] - llist[i+1][j])
    res += llist[0][j] + llist[-1][j]    

print(res + n*m*2)