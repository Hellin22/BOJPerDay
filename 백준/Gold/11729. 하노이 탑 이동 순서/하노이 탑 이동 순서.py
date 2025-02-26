import sys
inp = sys.stdin.readline
n = int(inp().strip())
llist = []
def hanoi(n, frrom, to, by):
    if n == 1:
        print(frrom, to)
        # llist.append([frrom, to])
        return
    
    hanoi(n-1, frrom, by, to)
    print(frrom, to)
    # hanoi(1, frrom, to, by)
    hanoi(n-1, by, to, frrom)

# print(len(llist))
print(2**n-1)
hanoi(n, 1, 3, 2)
# for i in range(len(llist)):
    # print(llist[i][0], llist[i][1])