import sys
inp = sys.stdin.readline

cnt = int(inp().strip())

arr = [*map(int, inp().strip().split())]
# arr = [list(map(int, inp().strip().split()))]
# arr의 끝에서부터 stck에 집어넣으면서 현재 idx의 데이터보다 스택에 잇는게 작으면 빼내기
stck = []
nge = [0] * cnt
for i in range(cnt-1, -1, -1):
    if not stck:
        stck.append(i)

    else:
        while stck and arr[stck[-1]] <= arr[i]:
            lastNumIdx = stck[-1]
            lastNumIdx = stck.pop()
            nge[lastNumIdx] = i+1
        stck.append(i)
for i in range(cnt):
    print(nge[i], end=' ')