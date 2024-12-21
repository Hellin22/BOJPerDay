import sys
inp = sys.stdin.readline

a,b = map(int, inp().split())

arr = map(int, inp().split())

res = []

for i in arr:
    if(i < b):
        res.append(i)

for i in res:
    print(i, end=" ")
