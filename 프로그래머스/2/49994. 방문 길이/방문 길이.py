'''
처음 걸어본 길이의 합 -> 그냥 탐색문제
만약 범위 벗어나면 안함 -> 범위가 얼마? (5, 5)로 구성.
(5, 5)에서 시작한다고 가정?
visit = [11][11][4]
'''

def solution(dirs):
    answer=0
    n = 10
    dt = {"U":(1, 0), "D":(-1, 0), "R":(0, 1), "L":(0, -1)}
    dt2 = {"U":0, "R":1, "D":2, "L":3}
    curx, cury = 5, 5
    visit = [[[0]*4 for _ in range(n+1)] for _ in range(n+1)]
    for i, val in enumerate(dirs):
        nx, ny = curx + dt[val][0], cury + dt[val][1]
        if 0<=nx<=n and 0<=ny<=n:
            if visit[curx][cury][dt2[val]] != 1: 
                answer+=1
                visit[curx][cury][dt2[val]] = 1
                visit[nx][ny][(dt2[val]+2)%4] = 1
            # cur -> nx
            curx, cury = nx, ny
    return answer