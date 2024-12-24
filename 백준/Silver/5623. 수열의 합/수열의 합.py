import sys
inp = sys.stdin.readline

n = int(inp().strip())
if n == 2:
    print(' '.join(map(str, [1, 1])))
    exit()

arr = [None] + [[None] + list(map(int, inp().strip().split())) for _ in range(n)]
res = [0] * (n + 1)

for i in range(1, n+1):
    a, b = i+1, i+2

    if(i+1 > n):
        a = i-1
    if(i+2 > n):
        if(a == i-1):
            b = i-2
        else: b = i-1
    
    res[i] = (arr[i][a] + arr[i][b] - arr[a][b]) / 2

print(" ".join(map(str, map(int, res[1:]))))
