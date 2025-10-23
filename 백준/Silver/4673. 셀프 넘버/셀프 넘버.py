import sys
inp = sys.stdin.readline

# 10000 이하 생성자가 없는 숫자.
# n -> d(n)은 n과 n자리 수를 더하는 함수
# d(75) = 75+7+5 = 87
# 완탐하면 될거같은데
# 100보다 작은 셀프 넘버는 1 3 5 7 9 ...
# 2는 왜 셀프넘버 아님? -> d(1) = 2라서 그런가?

visit = [0] * 10001
# visit[i]가 0이면 진행. 1이면 안해도됨. (이미 다른 수가 처리한 수)
# 각 자리수만 더하는것. 999면 99를 더하지는 않음.
answer = []

def dfs(cnt, i):
    if i > 10000 or visit[i] == 1: return
    
    if cnt != 0:
      visit[i] = 1
    # i와 i의 자리수 합
    new_n = i + sum([int(str(i)[j]) for j in range(len(str(i)))])
    dfs(cnt+1, new_n)


for i in range(10001):
    if visit[i] == 1: continue # 1이면 처리 안함.
    
    dfs(0, i)

ans_list = []
for i in range(1, 10001):
    if visit[i] == 0:
      ans_list.append(i)
print("\n".join(map(str, ans_list)))