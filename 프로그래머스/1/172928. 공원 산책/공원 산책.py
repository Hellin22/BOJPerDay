'''
["방향, 거리", "방향, 거리"] 이중 string이 여러개 들어옴

E 5는 현재 위치에서 동쪽으로 5칸 이동

1. 이동시 공원 벗어나는지?
2. 장애물을 만나는지?

둘중 하나라도 O -> 무시
아니라면 이동

'''



        
        

def solution(park, routes):
    answer = []
    n, m = len(park), len(park[0])
    cx, cy = 0, 0
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                cx, cy = i, j
    
    def check(x, y, dirr, dist, n, m):
        dt = {"E": 0, "S": 1, "W": 2, "N": 3}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        nx, ny = x + directions[dt[dirr]][0]*dist, y + directions[dt[dirr]][1]*dist
        if nx < 0 or ny < 0 or nx >= n or ny >= m: 
            return x, y
        else:
            '''
            ["OXO", 
             "XSX", 
             "OXO"]
            
            '''
            print(" ")
            for i in range(min(x, nx), max(x, nx)+1):    
                for j in range(min(y, ny), max(y, ny)+1):
                    if park[i][j] == "X": return x, y
                
            return nx, ny
            
                    
    for st in routes:
        e, s = st.split(" ")
        cx, cy = check(cx, cy, e, int(s), n, m)
    return [cx, cy]