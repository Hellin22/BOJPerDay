import sys
inp = sys.stdin.readline
n, k, p, x = map(int, inp().strip().split())
res = 0
str_n, str_x = list(str(n)), list(str(x))

while len(str_n) > len(str_x):
    # str_x 앞에다가 0으로 채워줘야함
    str_x.insert(0, "0")

dp = [[0] * 10 for _ in range(10)]
dp[0] = [0, 4, 3, 3, 4, 3, 2, 3, 1, 2]
dp[1] = [0, 0, 5, 3, 2, 5, 6, 1, 5, 4]
dp[2] = [0, 0, 0, 2, 5, 4, 3, 4, 2, 3]
dp[3] = [0, 0, 0, 0, 3, 2, 3, 2, 2, 1]
dp[4] = [0, 0, 0, 0, 0, 3, 4, 3, 3, 2]
dp[5] = [0, 0, 0, 0, 0, 0, 1, 4, 2, 1]
dp[6] = [0, 0, 0, 0, 0, 0, 0, 5, 1, 2]
dp[7] = [0, 0, 0, 0, 0, 0, 0, 0, 4, 3]
dp[8] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
dp[9] = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0]


def dfs(cur_i, cur_p , critical, zero_cnt):
    global str_x, str_n, res, n, k, p, x
    # cur_p는 현재 얼마나 썼는지 -> 최대 p개임
    if cur_p > p: return
    if cur_i == len(str_x): 
        if zero_cnt == len(str_x): return
        if cur_p >= 1: res+=1
        return
    # 만약 종료 조건이 아니라면
    if critical == 1:
        for i in range(0, int(str_n[cur_i])+1):
            minn = min(int(str_x[cur_i]), i)
            maxx = max(int(str_x[cur_i]), i)
            if int(str_n[cur_i]) == i: # critical이 되는것
                if i == 0:
                    dfs(cur_i+1, cur_p+dp[minn][maxx], 1, zero_cnt+1)
                else:
                    dfs(cur_i+1, cur_p+dp[minn][maxx], 1, zero_cnt)
            else:
                if i == 0:
                    dfs(cur_i+1, cur_p+dp[minn][maxx], 0, zero_cnt+1)
                else:
                    dfs(cur_i+1, cur_p+dp[minn][maxx], 0, zero_cnt)

    else: # critical이 절대로 1이 안됨
        for i in range(0, 10):
            minn = min(int(str_x[cur_i]), i)
            maxx = max(int(str_x[cur_i]), i)
            if i == 0:
                dfs(cur_i+1, cur_p+dp[minn][maxx], 0, zero_cnt+1)
            else:
                dfs(cur_i+1, cur_p+dp[minn][maxx], 0, zero_cnt)

for i in range(int(str_n[0])):
    minn = min(int(str_x[0]), i)
    maxx = max(int(str_x[0]), i)
    if i == 0:
        dfs(1, dp[minn][maxx], 0, 1)
    else:
        dfs(1, dp[minn][maxx], 0, 0)

# critical할 때 처음에 0이 올 경우는 없음
dfs(1, dp[int(str_x[0])][int(str_n[0])], 1, 0)

print(res)