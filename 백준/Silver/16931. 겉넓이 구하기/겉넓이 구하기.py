import sys
inp = sys.stdin.readline

n, m = map(int, inp().strip().split())

llist = [list(map(int, inp().strip().split())) for _ in range(n)]
# 입력으로 받은것의 개수는 m임 -> n, m은 동일한가? 아님

res = 0

for i in range(len(llist)):
    for j in range(len(llist[i]) - 1):
        # j와 j+1로 하기
        plusNum = llist[i][j] - llist[i][j+1]
        if(plusNum > 0): res += plusNum
        else: res += plusNum * -1
    
    # 마지막에 양 끝 더해주기
    res += llist[i][0]
    res += llist[i][-1]

for j in range(m):
    for i in range(n-1):
        # j와 j+1로 하기
        plusNum = llist[i][j] - llist[i+1][j]
        if(plusNum > 0): res += plusNum
        else: res += plusNum * -1
    
    # 마지막에 양 끝 더해주기
    res += llist[0][j]
    res += llist[-1][j]

print(res + n*m*2)