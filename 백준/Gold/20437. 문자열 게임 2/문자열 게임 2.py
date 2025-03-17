import sys
inp = sys.stdin.readline

t = int(inp().strip())

for _ in range(t):
    sttr = inp().strip()
    k = int(inp().strip())

    alphabet = [[] for _ in range(26)]
    for i in range(len(sttr)):
        alphabet[ord(sttr[i])-97].append(i)
    res1 = 10001
    res2 = -1
    for i in range(26):
        if len(alphabet[i]) >= k:
            for j in range(len(alphabet[i])-k+1):
                # 0 1 2 3
                # j, j+k-1
                res1 = min(res1, alphabet[i][j+k-1]-alphabet[i][j]+1)
                res2 = max(res2, alphabet[i][j+k-1]-alphabet[i][j]+1)
    print(-1 if res2 == -1 or res1 == 10001 else f"{res1} {res2}")