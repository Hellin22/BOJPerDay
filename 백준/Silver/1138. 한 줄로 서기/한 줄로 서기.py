import sys

inp = sys.stdin.readline

n = int(inp())
arr = [0] * (n+2) # 사람들 번호가 들어갈 곳이다
height_cnt = [0] + list(map(int, inp().strip().split()))
arr[1] = n # 키큰사람을 젤 앞에 박아놓고 시작
for i in range(len(height_cnt)-2, 0, -1): # 키큰순부터 작은순으로
    cnt = 0
    for j in range(1, n+1): # arr의 1번부터 전부 돌거임
        if cnt == height_cnt[i]:
            for k in range(n+1, j, -1):
                arr[k] = arr[k-1]
            arr[j] = i
            break
        else: # i는 현재 키, arr[j]는 거기 들어있는 사람의 키
            if i > arr[j]: # 내가 더 큼 -> continue
                continue
            else: # 키 더 작음. 같을순 없음
                cnt+=1
    
print(' '.join(map(str, arr[1:n+1])))