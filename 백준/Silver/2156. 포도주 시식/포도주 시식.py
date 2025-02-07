import sys
inp = sys.stdin.readline

n = int(inp())
grapes = [int(inp()) for _ in range(n)]

arr = [[0] *  n for _ in range(3)]

if n == 1:
    print(grapes[0])
    exit()
elif n == 2:
    print(grapes[0] + grapes[1])
    exit()

arr[0][0] = 0
arr[1][0] = grapes[0]
arr[2][0] = 0
arr[0][1] = arr[0][0]
arr[1][1] = arr[0][0] + grapes[1]
arr[2][1] = arr[1][0] + grapes[1]

for i in range(2, n):
    arr[0][i] = max(arr[0][i-1], arr[1][i-2], arr[2][i-1])
    arr[1][i] = max(arr[0][i-1], arr[1][i-2], arr[2][i-2]) + grapes[i] # 현재 하나 먹은것 == i-2에서의 최대값도 가능
    arr[2][i] = arr[1][i-1] + grapes[i]
print(max(arr[0][n-1], arr[1][n-1], arr[2][n-1]))