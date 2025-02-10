import sys
inp = sys.stdin.readline

n = int(inp())
arr = [0] * n
dist = [0] * n
res = 0
for i in range(n):
    arr[i] = int(inp())

stck = []
for i in range(n):
    if not stck:
        stck.append(i)
    else:
        while stck and arr[stck[-1]] <= arr[i]:
            if stck[-1] == arr[i]: 
                dist[stck[-1]] == 0
            else:
                res+=(i-stck[-1]-1)
                dist[stck[-1]] = (i-stck[-1]-1)
            stck.pop()
        stck.append(i)
for i in range(len(stck)-2, -1, -1):
    res += (stck[-1] - stck[i])
    dist[stck[i]] = (stck[-1] - stck[i])

print(res)