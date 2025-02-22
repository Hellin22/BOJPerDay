import sys
inp = sys.stdin.readline

n = int(inp().strip())
# 10000까지 진행?
arr = [[0] * 100001 for _ in range(3)]
arr[0][1] = 1
arr[1][1] = 0
arr[2][1] = 0
arr[0][2] = 1
arr[1][2] = 1
arr[2][2] = 0

for j in range(3, 10001):
    arr[0][j] = arr[0][j-1] + arr[1][j-1] + arr[2][j-1]#sum(arr[i-1][0], arr[i-1][1], arr[i-1][2])
    arr[1][j] = arr[1][j-2]+ arr[2][j-2]
    arr[2][j] = 1 if j % 3 == 0 else 0

for i in range(n):
    k = int(inp().strip())
    print(arr[0][k] + arr[1][k] + arr[2][k])