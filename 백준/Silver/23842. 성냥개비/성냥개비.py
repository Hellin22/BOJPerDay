import sys
inp = sys.stdin.readline

n = int(inp().strip())

dp = [0] * 100 # (0~99)

dp[0] = 12
dp[1] = 8
dp[2] = 11
dp[3] = 11
dp[4] = 10
dp[5] = 11
dp[6] = 12
dp[7] = 9
dp[8] = 13
dp[9] = 12

for i in range(10, 100):
    fir, sec = str(i)[0], str(i)[1] # 1 0 이 각각 배정
    dp[i] = dp[int(fir)] + dp[int(sec)] - 12

for i in range(100):
    for j in range(i, 100):
        if i+j >= 100: break
        # if dp[i] + dp[j] != n - 4: continue # 이렇게 하면 안되지. 3개가 있어야하니까
        else:
            # 여기서 성냥개비 수가 n-4개와 같은지 확인 필요
            k = i + j
            # print(k)
            if (dp[i] + dp[j] + dp[k]) == n - 4: 

                ii = str(i)
                jj = str(j)
                kk = str(k)
                if i >= 0 and i <= 9:
                    ii = '0' + ii
                if j >= 0 and j <= 9:
                    jj = '0' + jj
                if k >= 0 and j <= 9:
                    kk = '0' + kk
                print(''.join([ii, "+", jj, "=", kk]))
                exit()

print("impossible")