import sys

inp = sys.stdin.readline

m, t = map(int, (inp().strip().split()))

arr = [[0] * (m+1) for _ in range(m+1)] # m+1 * m+1
dir = 0 # 현재 dir은 남 / 남동서북 순으로 진행
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
curx, cury = 0, 0
while t > 0:
    t-=1
    nOrder = inp().strip().split()

    order = nOrder[0] # 어떤 명령어인지(str)
    cnt = int(nOrder[1]) # 해당 명령이 몇번 하는지(int)

    if order == "MOVE": # 0~m까지 가능
        nx, ny = curx + dx[dir]* cnt, cury + dy[dir] * cnt

        if(nx < 0 or ny < 0 or nx > m or ny > m): 
            print(-1)
            exit()
        
        else:
            curx, cury = curx + dx[dir]* cnt, cury + dy[dir] * cnt

    else: # turn인 경우
        if cnt == 0:
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4
    
print(curx, cury)

