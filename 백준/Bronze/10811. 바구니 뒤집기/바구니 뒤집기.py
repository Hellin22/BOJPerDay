import sys
inp = sys.stdin.readline

n,m = map(int, inp().split())
arr = [i for i in range(n+1)]

for i in range(m):
    a, b = map(int, inp().split())
    arr[a:b+1] = arr[a:b+1][::-1]

print(" ".join(map(str,arr[1:])))