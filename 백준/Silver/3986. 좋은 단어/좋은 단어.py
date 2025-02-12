import sys
inp = sys.stdin.readline

n = int(inp())
arr = [inp().strip() for _ in range(n)]

res = 0
for i in range(n):
    stck = []
    for j in range(len(arr[i])):
        if not stck:
            stck.append(arr[i][j])
        else:
            if stck[-1] == arr[i][j]: stck.pop()
            else: stck.append(arr[i][j])
    if not stck: res+=1
print(res)