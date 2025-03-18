import sys
inp = sys.stdin.readline

def dfs(cur):
    global n
    if cur == n+1:
        res_str = "".join(str(x) for x in llist)
        res = res_str.replace(" ", "")
        res = eval(res)
        if res == 0:
            res_list.append(res_str)
        return

    llist.append("+")
    llist.append(str(cur))
    dfs(cur+1)
    llist.pop()
    llist.pop()

    llist.append("-")   
    llist.append(str(cur))
    dfs(cur+1)
    llist.pop()
    llist.pop()

    llist.append(" ")
    llist.append(str(cur))
    dfs(cur+1)
    llist.pop()
    llist.pop()


t = int(inp().strip())

for _ in range(t):
    res_list = []
    llist = ["1"]
    n = int(inp().strip())
    dfs(2)

    res_list.sort()
    print("\n".join(res_list))
    print()

