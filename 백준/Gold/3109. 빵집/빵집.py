import sys
inp = sys.stdin.readline


'''
첫째  열은 근처 빵집의 가스관

마지막 열은 원웅이 빵집

건물이 있으면 못놓음

첫째열 시작 + 마지막 열 끝

오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선

겹치면 안되고 접하면 안됨. 칸을 지나는 파이프는 하나

파이프라인의 최대개수


'''

# 오른쪽 위, 오른쪽 아래 우선
# 그게 안되면 오른쪽. 그것도 안되면 종료
# 겹치면 안됨. -> 겹친다의 정의가 대각선 크로스는 되는거같음

# 1번쨰 열 -> n번째 열까지
# 위 아래 우선순위는 상관 없을듯? 해보고 판단

n, m = map(int, inp().strip().split())

arr = [[0] * m for _ in range(n)]

for i in range(n):
    llist = list(inp().strip())
    for j in range(len(llist)):
        arr[i][j] = llist[j]


visit = [[0]*m for _ in range(n)] # 방문 배열


ans = 0
flag = False
# 3번 반복할 지점 = (idxi, idxj)
def find(idxi, idxj):
    global n, m, ans, flag, pipe_list

    # 종료조건
    if idxj == m-1:
        ans+=1
        return True
    
    for tmp_i, tmp_j in [(idxi-1, idxj+1), (idxi, idxj+1), (idxi+1, idxj+1)]:
        if tmp_i < 0 or tmp_i >= n or tmp_j >= m or visit[tmp_i][tmp_j] == 1 or arr[tmp_i][tmp_j] == 'x': continue
        visit[tmp_i][tmp_j] = 1
        # True라면 길을 찾은것 -> 더이상 하면 안됨.
        # False라면 3번 모두 갔는데도 안된거니까 False 리턴
        if find(tmp_i, tmp_j):
            return True
        

    return False

# 처음 시작점에 따라서 우선순위가 바뀌는건가?
# 현재 i가 시작했을 때의 행보다 작으면 

# 제일 위에꺼부터 시작
for i in range(n):
    find(i, 0) # i, 0에 대해서 find 시작

print(ans)

