import sys
inp = sys.stdin.readline

arr = [0]*31 # 0~30

for i in range(28):
    a = int(inp().strip())
    arr[a] = 1

for i in range(1, 31):
    if(arr[i] == 0):
        print(i)

