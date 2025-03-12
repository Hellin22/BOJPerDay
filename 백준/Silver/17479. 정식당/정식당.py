import sys
inp = sys.stdin.readline

a, b, c = map(int, inp().strip().split())

dictt = dict()
cur_price = 0
for i in range(a):
    st, pr = inp().strip().split()
    dictt[st] = (0, int(pr))

for i in range(b):
    st, pr = inp().strip().split()
    dictt[st] = (1, int(pr))

for i in range(c):
    st= inp().strip()
    dictt[st] = (2, )

k = int(inp().strip())

ilban_cnt = 0
ilban_mon = 0

spec_cnt = 0
spec_mon = 0

ser_cnt = 0
for i in range(k):
    st = inp().strip()
    if dictt[st][0] == 0: # 일반 음식
        ilban_cnt+=1
        ilban_mon+=dictt[st][1]
    elif dictt[st][0] == 1: # 특별음식
        spec_cnt+=1
        spec_mon+=dictt[st][1]
    else:
        ser_cnt+=1

flag = True
if ser_cnt >= 2:
    flag = False
elif ilban_mon + spec_mon < 50000 and ser_cnt == 1:
    flag = False
elif ilban_mon < 20000 and spec_mon != 0:
    flag = False

print("Okay" if flag else "No")