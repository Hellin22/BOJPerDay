'''
123
456
789
101112

-> left와 right의 값을 가지고 있어야함. + 맨해튼 거리 사용하기

left, right = 10, 12
lx, ly, rx, ry = 3, 0, 3, 2

'''

def solution(numbers, hand):
    answer = ''
    
    arr = [[j + i * 3 for j in range(1, 4)] for i in range(4)]
    dt = {"1" : (0, 0), "2" : (0, 1), "3" : (0, 2), "4" : (1, 0), "5" : (1, 1), "6": (1, 2), "7" : (2, 0), "8" : (2, 1), "9" : (2, 2), "0" : (3, 1)}
    
    lx, ly, rx, ry = 3, 0, 3, 2
    
    
    for i, val in enumerate(numbers):
        cur = val
        cx, cy = dt[str(cur)]
        c = -1
        if val in (1, 4, 7):
            lx, ly = dt[str(cur)]
            c = 0
        elif val in (3, 6, 9):
            rx, ry = dt[str(cur)]
            c = 1
        else: # 중앙
            lab, rab = abs(lx - cx) + abs(ly - cy), abs(rx - cx) + abs(ry - cy)
            if lab < rab: 
                lx, ly = dt[str(cur)]
                c = 0
            elif rab < lab: 
                rx, ry = dt[str(cur)]
                c = 1
            else: # 거리가 동일함
                if hand == "right": 
                    rx, ry = dt[str(cur)]
                    c = 1
                else: 
                    lx, ly = dt[str(cur)] 
                    c = 0
        answer += "L" if c == 0 else "R"
    return answer