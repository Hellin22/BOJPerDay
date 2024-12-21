import sys
inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = [i+1 for i in range(n)]
for i in range(m):
    a,b = map(int, inp().split())
    tmp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = tmp

print(" ".join(map(str, arr)))