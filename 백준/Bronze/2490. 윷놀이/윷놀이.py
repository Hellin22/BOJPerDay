import sys
inp = sys.stdin.readline

for _ in range(3):
    llist = list(map(int, inp().strip().split()))
    onee = 0
    for i in range(4):
        if llist[i] == 1: onee+=1
    if onee == 3:
        print("A")
    elif onee == 2:
        print("B")
    elif onee == 1:
        print("C")
    elif onee == 0:
        print("D")
    else:
        print("E")