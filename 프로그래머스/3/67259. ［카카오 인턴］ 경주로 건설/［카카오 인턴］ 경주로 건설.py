cost = 99999999999

def DFS(board, curmoney,direct,x,y, length, waycost) :
    global cost
    board[x][y] = 1
    if waycost[x][y] == -1 :
        waycost[x][y] = curmoney
    else :
        if waycost[x][y]+400 < curmoney :
            return
        else : 
            waycost[x][y] = curmoney
    if (x, y) == (length-1,length-1) :
        if cost>curmoney :
            cost = curmoney
        return
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    for d in direction :
        newx = x+d[0]
        newy = y +d[1]
        if max(newx,newy)<length and min(newx,newy) >=0 and board[newx][newy] == 0:
            newcurmoney = curmoney + 100 if direct == d else curmoney + 600
            DFS(board, newcurmoney, d, newx,newy, length, waycost)
            board[newx][newy] = 0

def solution(board):
    global cost
    board[0][0]=1
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    length = len(board)
    waycost = [[-1 for i in range(length)] for i in range(length)]
    waycost[0][0] = 0
    for d in direction :
        newx = d[0]
        newy = d[1]
        if max(newx, newy) < length and min(newx, newy) >= 0 and board[newx][newy] == 0:
            DFS(board, 100, d, newx, newy, length, waycost)
            board[newx][newy] = 0
    return cost
