import sys

inp = sys.stdin.readline
n = int(inp())
arr = list(map(int, inp().split()))
curl, curr = 0, n-1
cur = arr[curr]+arr[curl]
resl, resr = curl, curr
rescur = arr[curr]+arr[curl]

while(curr > curl):
    if abs(curr-curl) == 1: break
    if cur > 0: curr-=1
    else: curl+=1

    cur = arr[curr]+arr[curl]
    if abs(rescur) >= abs(cur):
        resl, resr = curl, curr
        rescur = cur

print(arr[resl], arr[resr])