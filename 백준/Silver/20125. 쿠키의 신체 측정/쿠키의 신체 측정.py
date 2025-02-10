import sys
inp = sys.stdin.readline

n = int(inp())
arr = [[0]*n for _ in range(n)]
dx, dy = [0, 1, 0, -1],[1, 0, -1, 0]
for i in range(n):
    strs = inp()
    for j in range(n):
        if strs[j] == "_": arr[i][j] = 0
        else: arr[i][j] = 1
heartx, hearty = -1, -1
for i in range(n):
    flag = True
    for j in range(n):
        flag = True
        if arr[i][j] == 0:
            flag = False
            continue
        for k in range(4):
            nx, ny = dx[k] + i, dy[k] + j
            if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] == 0:
                flag = False
                break
        if flag: 
            heartx, hearty = i, j
            break
    if flag: break
# 심장 좌표 구함.
leftHand, rightHand, waist, leftLeg, rightLeg = 0, 0, 0, 0, 0
for j in range(hearty-1, -1, -1):
    if arr[heartx][j] == 1: leftHand+=1
    else: break
for j in range(hearty+1, n, 1):
    if arr[heartx][j] == 1: rightHand+=1
    else: break
for i in range(heartx+1, n, 1):
    if arr[i][hearty] == 1: waist+=1
    else: break
for i in range(heartx + waist + 1, n, 1):
    if arr[i][hearty-1] == 1: leftLeg+=1
    else: break
for i in range(heartx + waist + 1, n, 1):
    if arr[i][hearty+1] == 1: rightLeg+=1
    else: break

print(f"{heartx+1} {hearty+1} \n{leftHand} {rightHand} {waist} {leftLeg} {rightLeg}")