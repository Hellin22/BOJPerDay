'''
결국 제일 작은 x, y
제일 큰 x, y를 찾으면 되는 문제임

이걸 어떻게 할 것인가?
[".#...", 
 "..#..", 
 "...#."]
 아 제일 큰거는 +1, +1 해주면 되는거 같은데?
 0,1 2, 3-> 3, 4로 해주면 됨.
 
 ["..",
  "#."]
1,0 1,0 -> 10 21
'''

def solution(wallpaper):    
    sx, sy, lx, ly = 100, 100, -1, -1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                sx, sy = min(sx, i), min(sy, j)                
                lx, ly = max(lx, i), max(ly, j)

    return [sx, sy, lx+1, ly+1]