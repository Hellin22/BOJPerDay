import sys
inp = sys.stdin.readline

# n은 2의 제곱수
n = int(inp().strip())
arr = [list(map(int, inp().strip().split())) for _ in range(n)]
llist = [0, 0]
def recursion(cur, x, y):
    if cur == 1:
        llist[arr[x][y]] +=1
        return
    
    k = arr[x][y]
    flag = True
    for i in range(x, x+cur):
        for j in range(y, y+cur):
            if k != arr[i][j]:
                flag = False
                break
        if flag is False: break
    
    if flag: # 모두 동일한것
        llist[k]+=1
    else:
        cur//=2
        for i in range(2):
            for j in range(2):
                recursion(cur, x+i*cur, y+j*cur)

recursion(n, 0, 0)
print("\n".join(map(str, llist)))