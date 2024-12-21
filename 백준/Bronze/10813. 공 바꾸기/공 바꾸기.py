import sys
inp = sys.stdin.readline

n, m = map(int, inp().split())

arr = [i+1 for i in range(n)]
for i in range(m):
    a,b = map(int, inp().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

print(" ".join(map(str, arr)))