import sys
inp = sys.stdin.readline

n = int(inp().strip())
arr = [list(map(int, inp().strip().split())) for _ in range(n)]
llist = [0] * 3

def recursion(cur, x, y): # 한칸의 길이, 시작 위치(x y)
    if cur == 1:
        llist[arr[x][y]] += 1
        return
    else: 
        k = arr[x][y]
        flag = True
        for i in range(x, x+cur):
            for j in range(y, y+cur):
                if arr[i][j] != k: 
                    # cur//3
                    flag = False
                    break
            if flag is False: break
        
        if flag: # 다 똑같은 경우
            # print(cur, x, y, k)
            llist[k] += 1
        else:
            cur //=3
            for i in range(3):
                for j in range(3):
                    # print(cur, x+i*cur, y+j*cur)
                    recursion(cur, x+i*cur, y+j*cur)

recursion(n, 0, 0)
print(llist[-1], llist[0], llist[1])