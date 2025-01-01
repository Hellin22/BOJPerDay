import sys

inp = sys.stdin.readline
res = []

# 입력이 0이 나오면 종료
while True:
    m = int(inp().strip())
    if m == 0: break
    line = inp().strip()
    chars = [0] * 128

    ddict = dict()
    maxx, left, curCnt = -1, 0, 0
    for right in range(len(line)):
        charasci = ord(line[right])
        chars[charasci]+=1
        if(chars[charasci] == 1): curCnt+=1

        if(curCnt > m):
            charasci = ord(line[left])
            chars[charasci]-=1
            left+=1
            if(chars[charasci] == 0): curCnt-=1

        else: maxx = max(maxx, right - left + 1)
    res.append(maxx)

for i in res:
    print(i)