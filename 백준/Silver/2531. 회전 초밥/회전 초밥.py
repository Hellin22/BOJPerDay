import sys
inp = sys.stdin.readline
n, d, k, c = map(int, inp().strip().split())

res = -1
arr = [int(inp().strip()) for _ in range(n)]

chobab_dict = {}
for i in range(k):
    chobab_dict[arr[i]] = chobab_dict.get(arr[i], 0)+1

res = len(chobab_dict.keys())

left, right = 0, k-1
for _ in range(n):
    right = (right+1) % n
    if arr[right] not in chobab_dict.keys():
        chobab_dict[arr[right]] = 1
    else: chobab_dict[arr[right]]+=1
    if chobab_dict[arr[left]] == 1:
        chobab_dict.pop(arr[left])
    else: chobab_dict[arr[left]]-=1
    left+=1
    curres = len(chobab_dict.keys())
    if c not in chobab_dict.keys(): curres+=1
    res = max(res, curres)
print(res)