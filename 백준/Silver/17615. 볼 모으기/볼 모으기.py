import sys
inp = sys.stdin.readline

n = int(inp())
strr = inp().strip()

if len(strr) == 1: 
    print(0)
    exit()
# 그냥 왼쪽, 오른쪽으로 데이터를 몰때의 최소값 판별? -> 이게 알고리즘이 쓰이는건가?
# 4번 할거고 50만이라 복잡도도 오래걸리지 않는듯?

# 1. 왼쪽에 R 몰기 -> 처음 B 만난다면 flag를 true -> 그후에 R 만나면 +=1
res = 500001
curres = 0
flag = True
for i in range(n): # R 왼쪽
    if strr[i] == "B": 
        flag = False
        continue
    # 여기는 R인 경우
    if flag: continue # 처음 연속된 R의 경우 카운트x
    
    curres+=1
res = min(res, curres)

curres = 0
flag = True
for i in range(n): # B 왼쪽
    if strr[i] == "R": 
        flag = False
        continue
    # 여기는 R인 경우
    if flag: continue # 처음 연속된 R의 경우 카운트x
    
    curres+=1
res = min(res, curres)

curres = 0
flag = True
for i in range(n-1, -1, -1): # R오른쪽
    if strr[i] == "B":
        flag = False
        continue
    if flag: continue

    curres+=1
res = min(res, curres)

curres = 0
flag = True
for i in range(n-1, -1, -1): 
    if strr[i] == "R":
        flag = False
        continue
    if flag: continue

    curres+=1
res = min(res, curres)

print(res)