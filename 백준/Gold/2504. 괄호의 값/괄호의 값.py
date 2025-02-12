import sys
inp = sys.stdin.readline

stck = []
llist = list(inp().strip())

for ch in llist:
    if ch == "(" or ch == "[":
        stck.append(ch)
    elif ch == ")":
        if not stck or stck[-1] == "[": 
            print(0)
            exit()
        elif stck and stck[-1] == "(": # 숫자가 아님
            stck.pop()
            stck.append(2)
        else: # 숫자
            if len(stck) >= 2 and stck[-2] == "(":
                num = stck.pop()
                stck.pop()
                stck.append(num*2)
            else: 
                print(0)
                exit()
    elif ch == "]":
        if not stck or stck[-1] == "(":
            print(0)
            exit()
        elif stck and stck[-1] == "[":
            stck.pop()
            stck.append(3)
        else:
            if len(stck) >= 2 and stck[-2] == "[":
                num = stck.pop()
                stck.pop()
                stck.append(num*3)
            else: 
                print(0)
                exit()
    if len(stck) >= 2 and stck[-1] != "(" and stck[-1] != "[" and stck[-2] != "(" and stck[-2] != "[":
        n1, n2 = stck.pop(), stck.pop()
        stck.append(n1+n2)

if len(stck) > 1 or stck[0] == "(" or stck[0] == "[":
    print(0)
else:
    print(stck[0])

