import sys
inp = sys.stdin.readline

res = -1
n = int(inp())
arr = list(map(int, inp().split()))

wantNum = int(inp())
# s, e는 돈 금액임. -> arr의 최대값을 기준으로 삼아야함.
arr.sort()
s = 0
e = arr[n-1]

while s<=e:
    m = (s+e)//2

    # 곱 저장할 반복문
    minusAllPlus = 0
    for i in range(n):

        # minusNum = arr[i] - m
        if arr[i] >= m: minusAllPlus+=m
        else: minusAllPlus+=arr[i]
    if minusAllPlus == wantNum: 
        res = m
        break
    elif minusAllPlus < wantNum:
        res = max(res, m)
        s = m+1
    else:
        e = m-1
print(res)