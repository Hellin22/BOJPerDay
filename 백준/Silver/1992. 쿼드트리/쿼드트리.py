import sys
inp = sys.stdin.readline

llist = []
def recursion(cur, x, y):
    if cur == 1:
        llist.append(arr[x][y])
        return

    # 다시 recursion을 해야함 -> 4구역으로 나눠야함.
    flag = True
    for i in range(x, x+cur):
        for j in range(y, y+cur):
            if arr[i][j] != arr[x][y]:
                flag = False
                break
        if not flag: break
    
    if flag:
        llist.append(arr[x][y])
        return
    
    cur //= 2
    llist.append("(")
    recursion(cur, x, y)
    recursion(cur, x, y+cur)
    recursion(cur, x+cur, y)
    recursion(cur, x+cur, y+cur)
    llist.append(")")


n = int(inp().strip())
arr = [list(map(int, inp().strip())) for _ in range(n)]

recursion(n, 0, 0)
print("".join(map(str, llist)))