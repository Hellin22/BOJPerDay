import sys
inp = sys.stdin.readline
n = int(inp().strip())
llist = []
def hanoi(n, frrom, to, by):
    if n == 1:
        llist.append([frrom, to])
        return
    
    hanoi(n-1, frrom, by, to)
    hanoi(1, frrom, to, by)
    hanoi(n-1, by, to, frrom)

hanoi(n, 1, 3, 2)
print(len(llist))
for i in range(len(llist)):
    print(llist[i][0], llist[i][1])