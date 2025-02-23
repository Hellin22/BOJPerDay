import sys
inp = sys.stdin.readline
h, w = map(int, inp().strip().split())

arr = list(map(int, inp().strip().split()))

stck = []
stck.append(arr[0])
maxx = arr[0]
res = 0
for i in range(1, w):
    if arr[i] >= maxx:
        len_stck = len(stck)
        for k in range(len_stck):
            res += maxx - stck[-1]
            stck.pop()
        maxx = arr[i]
        stck.append(arr[i])
    else:
        stck.append(arr[i])

if stck: # 끝까지 갔는데 존재함. -> 제일 왼쪽(stck[0])이 가장 높은거라는 의미 -> 반대서부터 다시 시작
    arr = []
    stck = stck[::-1]
    # stck.reverse()
    arr.append(stck[0])
    maxx = stck[0]
    for i in range(1, len(stck)):
        if stck[i] >= maxx:
            len_stck = len(arr)
            for k in range(len_stck):
                res+=maxx-arr[-1]
                arr.pop()
            maxx = stck[i]
            arr.append(stck[i])
        else:
            arr.append(stck[i])

print(res)