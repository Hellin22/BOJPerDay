import sys
from collections import deque
inp = sys.stdin.readline

s = int(inp())
res = 0
q = deque()
clipboard = 0
cur = 1
visit = [[0] * (2*s+1) for _ in range(2*s + 1)]
q.append([cur, cur, 1])
q.append([clipboard, cur+clipboard, 1])
q.append([clipboard, cur-1, 1])
visit[cur][cur] = 1
visit[clipboard][cur+clipboard] = 1
visit[clipboard][cur-1] = 1
while q:
    curs = q.popleft()
    # 1. clipboard를 cur로 하고 1번 연산 (time++)
    q.append([curs[1], curs[1], curs[2]+1])

    # 2. cur+=clipboard -> 여기서 된다면 종료
    if curs[0] + curs[1] <= s and visit[curs[0]][curs[0]+curs[1]] == 0: # clip, cur 
        q.append([curs[0], curs[0]+curs[1], curs[2]+1])
        visit[curs[0]][curs[0]+curs[1]] = 1
        if curs[0]+curs[1] == s: 
            print(curs[2]+1)
            exit()

    # 3. 화면 이모티콘 하나 삭제
    if curs[1]-1 < 0: continue
    if visit[curs[0]][curs[1]-1] == 1: continue
    q.append([curs[0], curs[1]-1, curs[2]+1])
    visit[curs[0]][curs[1]-1] = 1
    if curs[1]-1 == s:
        print(curs[2]+1)
        exit()