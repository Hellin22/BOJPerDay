import sys
inp = sys.stdin.readline

n = int(inp())
arr = [0] * 201 # -100 ~ 100 (0 포함)

nums = map(int, inp().split())

for num in nums:
    arr[num+100]+=1

v=int(inp())
print(arr[v + 100])