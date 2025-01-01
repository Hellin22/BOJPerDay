import sys

inp = sys.stdin.readline

# 입력이 0이 나오면 종료
while True:
    m = int(inp().strip())
    if m == 0: exit()
    line = inp().strip()
    chars = [0] * 128

    ddict = dict()
    maxx, left, curCnt = -1, 0, 0
    for right in range(len(line)):
        charasci = ord(line[right])
        chars[charasci]+=1
        if(chars[charasci] == 1): curCnt+=1

        while(curCnt > m):
            charasci = ord(line[left])
            chars[charasci]-=1
            left+=1
            if(chars[charasci] == 0): curCnt-=1

        maxx = max(maxx, right - left + 1)
    print(maxx)
