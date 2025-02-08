import sys
inp = sys.stdin.readline

n = int(inp())

number = list(inp().strip())
wantNumber = list(inp().strip())
res = 123456789
def solve():
    global n
    res = 0
    number1 = list(number)
    wantNumber1 = list(wantNumber)
    # print(number1, wantNumber1)
    if number1 == wantNumber1: return 0
    for i in range(1, n-1):
        # print(number1[i], wantNumber1[i-1])
        if number1[i-1] == wantNumber1[i-1]: continue 
        res+=1
        number1[i-1] = '1' if number1[i-1] == '0' else '0'
        number1[i] = '1' if number1[i] == '0' else '0'
        number1[i+1] = '1' if number1[i+1] == '0' else '0'
    
    # print(res, number1, wantNumber1)

    if number1 == wantNumber1: return res
    return -1

if n == 2:
    if number == wantNumber:
        print(0)
    else:
        number[0] = '1' if number[0] == '0' else '0'
        number[1] = '1' if number[1] == '0' else '0'
        if number == wantNumber:
            print(1)
        else:
            print(-1)
    exit()
    

# 0
resNum = solve()
if resNum != -1:
    res = min(resNum, res)

# 0, 1 뒤집기
number[0] = '1' if number[0] == '0' else '0'
number[1] = '1' if number[1] == '0' else '0'
resNum2 = solve()
if resNum2 != -1:
    res = min(resNum2+1, res)

# 0, 1 뒤집기 + 마지막 뒤집기
number[0] = '1' if number[0] == '0' else '0'
number[1] = '1' if number[1] == '0' else '0'
number[n-1] = '1' if number[n-1] == '0' else '0'
number[n-2] = '1' if number[n-2] == '0' else '0'

resNum2 = solve()
if resNum2 != -1:
    res = min(resNum2+1, res)

# 둘다 뒤집기
number[0] = '1' if number[0] == '0' else '0'
number[1] = '1' if number[1] == '0' else '0'

resNum2 = solve()
if resNum2 != -1:
    res = min(resNum2+2, res)

if res == 123456789:
    print(-1)
else: print(res)


