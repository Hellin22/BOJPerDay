import sys
inp = sys.stdin.readline

n, m = map(int, inp().split())
arr = [0]*n

for i in range (m):
    a, b, c = map(int, inp().split())
    for j in range(a-1, b):
        arr[j] = c

print(" ".join(map(str, arr))) 