import sys
from collections import Counter
inp = sys.stdin.readline

n, x = map(int, inp().split()) # n일동안 + x일 연속
arr = list(map(int, inp().split()))
# x-1부터 시작하기
summ = [0] * n
for i in range(x):
    summ[x-1] += arr[i]
for i in range(x, n, 1): # 
    summ[i] = summ[i-1] + arr[i] - arr[i-x]

ct = Counter(summ)
max_key = max(ct.items(), key=lambda x:(x[0], x[1]))
if max_key[0] == 0:
    print(f"SAD")
else:
    print(f"{max_key[0]}\n{max_key[1]}")