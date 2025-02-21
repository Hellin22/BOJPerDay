import sys
inp = sys.stdin.readline

n, k = map(int, inp().strip().split())
arr = list(map(int, inp().strip().split()))
num = [0] * 100001
left, right = 0, 0
# right가 i인듯?
res = 0
for i in range(n):
    num[arr[i]]+=1
    while num[arr[i]] > k and left < i:
        num[arr[left]]-=1
        left+=1

    res = max(res, i-left+1)
    # right+=1
print(res)