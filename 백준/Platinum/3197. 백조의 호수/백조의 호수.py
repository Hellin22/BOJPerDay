import sys
from collections import deque

inp = sys.stdin.readline

n, m = map(int, inp().strip().split())
arr = [list(inp().strip()) for _ in range(n)]

# 방향 벡터 (상하좌우)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 백조, 얼음 녹이는 큐, 방문 배열
swan_q, next_swan_q = deque(), deque()
water_q, next_water_q = deque(), deque()
swan_visited = [[False] * m for _ in range(n)]
water_visited = [[False] * m for _ in range(n)]

# 백조의 시작 위치
swan_x, swan_y = -1, -1

# 초기 세팅 (백조 위치 및 물/얼음 판별)
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            if swan_x == -1:  # 첫 번째 백조
                swan_x, swan_y = i, j
                swan_q.append((i, j))
                swan_visited[i][j] = True
            water_q.append((i, j))  # 백조도 결국 물이므로 추가
            water_visited[i][j] = True
        elif arr[i][j] == ".":  # 물
            water_q.append((i, j))
            water_visited[i][j] = True

# 백조 이동 BFS (한 단계씩 수행)
def move_swan():
    while swan_q:
        x, y = swan_q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not swan_visited[nx][ny]:
                swan_visited[nx][ny] = True
                if arr[nx][ny] == "L":  # 다른 백조를 만남
                    return True
                elif arr[nx][ny] == ".":  # 물이면 바로 이동 가능
                    swan_q.append((nx, ny))
                else:  # 얼음이면 다음에 녹고 이동 가능
                    next_swan_q.append((nx, ny))
    return False

# 얼음 녹이기 BFS (한 단계씩 수행)
def melt_ice():
    while water_q:
        x, y = water_q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not water_visited[nx][ny]:
                if arr[nx][ny] == "X":  # 얼음이면 녹이기
                    arr[nx][ny] = "."
                    next_water_q.append((nx, ny))
                water_visited[nx][ny] = True

# BFS 실행
days = 0
while True:
    if move_swan():  # 백조가 만날 수 있으면 종료
        print(days)
        break
    melt_ice()  # 얼음 녹이기

    # 다음 날을 위한 큐 갱신
    swan_q, next_swan_q = next_swan_q, deque()
    water_q, next_water_q = next_water_q, deque()
    days += 1
