import sys

inp = sys.stdin.readline

n = int(inp().strip())

f = [0] * (n+1)
g = [0] * (n+1)

for i in range(1, n+1, 1): # i의 배수에 대하여
    for j in range(i, n+1, i):
        f[j] += i

for i in range(1, n+1):
    g[i] = g[i-1] + f[i]

print(g[n])