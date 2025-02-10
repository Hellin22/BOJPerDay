import sys
inp = sys.stdin.readline

tc = int(inp())
arr = [list(map(int, inp().split())) for _ in range(tc)]

for t in range(tc):
    cnt = 0
    idx = 1 # 2부터 하면됨
    for i in range(idx+1, 21):
        changeIdx = -1
        for j in range(i-1, 0, -1):
            if arr[t][j] < arr[t][i]: continue
            else: 
                changeIdx = j
        if changeIdx == -1: continue
        k = arr[t][i]
        for j in range(i, changeIdx, -1):
            arr[t][j] = arr[t][j-1]
            cnt+=1
        arr[t][changeIdx] = k
    print(f"{t+1} {cnt}")
