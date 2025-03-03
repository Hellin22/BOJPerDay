import sys
from collections import deque
inp = sys.stdin.readline

def dot_open(x, y): # 빈칸 열기 -> nx, ny를 보는게 아니다.
    global n, m
    visit[x][y] = 1
    dq.append((x, y))

def dollar(x, y):
    global n, m, res
    res+=1
    visit[x][y] = 1
    dq.append((x, y))

def lower_alpha(x, y):
    global n, m
    visit[x][y] = 1
    dq.append((x, y))
    for i in range(len(door_list[ord(arr[x][y].lower())-97])): # 그 키에대한 문들 해제해주기
        arr[door_list[ord(arr[x][y].lower())-97][i][0]][door_list[ord(arr[x][y].lower())-97][i][1]] = "."
        door_open(door_list[ord(arr[x][y].lower())-97][i][0], door_list[ord(arr[x][y].lower())-97][i][1])
    arr[x][y] = "."

def door_open(x, y):
    global n, m
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0<=nx<n and 0<= ny<m and visit[nx][ny] == 1:
            # 방문이 한번이라도 된 곳이라면?
            dq.appendleft((nx, ny))
            visit[nx][ny] = 1
    
    # 만약 가장자리였다면? 추가해줘야함. -> 이게 문제가 아니라 
    if (x, y) in coor:
        coor.remove((x, y))
        visit[x][y] == 1
        dq.appendleft((x, y))

t = int(inp().strip())
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(t):
    n, m = map(int, inp().strip().split())
    arr = [list(inp().strip()) for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    # 문서의 위치는 상관 없음
    # 대문자와 소문자를 구분해서 가지고 있어야함.
    # 소문자는 열쇠이고 대문자는 문임.
    # 소문자의 위치는 가지고 있을 필요 없을거같음.
    # 대문자의 위치만 저장해놓기
    dq = deque()
    key_list = [0] * 26 # lower
    door_list = [[] for _ in range(26)]
    res = 0
    
    '''
    0. 접근 가능한 가장자리를 모두 dq에 추가해주기
    1. 처음 주어지는 열쇠에 대한 존재유무 하는 배열 key_alpa[26] --- 0은 없음. 1은 있음
    2. arr 돌면서 만약 대문자이다.(isupper() is True) -> [].lower()이 1이라면 이미 열쇠 있다는뜼. 이거 고려안해줘도 될듯 
    3. 만약 대문자이면 [ord('A')-65]에는 여러개의 좌표가 있을텐데 그거 모두 빈칸으로 만들기
        + 빈칸으로 만들고 나서 사방에 visit가 하나라도 되어있었다면 res+=1 후에 append 해주기
        + 생각해보니 append나 appendleft나 상관 없을듯 뭘하든??
    '''
    coor = set()
    pre_keys = inp().strip()
    if pre_keys != "0":
        for key in pre_keys:
            key_list[ord(key)-97] = 1

    for i in range(n):
        for j in range(m):
            # 1. 만약 arr[i][j]가 "*, $, ."이 아닌경우
            if arr[i][j] not in ("*.$"):
                if arr[i][j].isupper(): # 만약 대문자라면? 문 좌표에 추가해야함.
                    if key_list[ord(arr[i][j].lower())-97] == 1: # 이미 열쇠 있다면 갈수있는 공간으로 만들기
                        arr[i][j] = "."
                    else:
                        door_list[ord(arr[i][j].lower())-97].append((i, j))


    # bfs 시작 -> 들어갈 수 있는 가장자리 모두 넣기
    for i in range(n):
        for j in range(m):
            if i != 0 and i != n-1:
                if 1<=j<=m-2: continue
            if arr[i][j] == ".":
                dot_open(i, j)
            elif arr[i][j] == "$":
                dollar(i, j)
            elif arr[i][j].isalpha():
                if arr[i][j].islower():
                    lower_alpha(i, j)
                elif arr[i][j].isupper():
                    coor.add((i, j))
    while dq:
        tx, ty = dq.popleft()
        # print()
        # for i in arr:
            # print(*i)
        # print()
        for dx, dy in directions:
            x, y = tx+dx, ty+dy
            # 갈수 있는곳
            if 0<=x<n and 0<=y<m and visit[x][y] == 0 and arr[x][y] != "*":
                if arr[x][y] == ".":
                    dot_open(x, y)
                elif arr[x][y] == "$":
                    dollar(x, y)
                elif arr[x][y].isalpha():
                    if arr[x][y].islower():
                        lower_alpha(x, y)
    print(res)