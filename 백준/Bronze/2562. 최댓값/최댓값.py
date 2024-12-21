import sys
inp = sys.stdin.readline

arr=[]
for i in range(9):
    arr.append(int(inp().strip()))

print(max(arr))
print(arr.index(max(arr))+1)