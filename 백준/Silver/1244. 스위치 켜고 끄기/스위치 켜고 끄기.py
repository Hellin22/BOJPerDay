import sys
'''
8
0 1 0 1 0 0 0 1
2
1 3 남
2 3 여

출력
1 0 0 0 1 1 0 1
'''
inp = sys.stdin.readline
switch_cnt = int(inp().strip())
switches = [0] + list(map(int, inp().strip().split()))
st_cnt = int(inp().strip())
for i in range(st_cnt):
    gender, switch_num = map(int, inp().strip().split())
    
    if gender == 1: # 남자인 경우
        for i in range(switch_num, switch_cnt + 1, switch_num):
            switches[i] = 1 if switches[i] == 0 else 0


    else: # 여자인 경우
        le, ri = switch_num, switch_num
        while True:
            if le == 0:
                le += 1
                ri -=1
                break
            elif ri == len(switches):
                le +=1
                ri -=1
                break
            elif switches[le] == switches[ri]:
                le-=1
                ri+=1
            elif switches[le] != switches[ri]:
                le+=1
                ri-=1
                break
        for i in range(le, ri+1):
            switches[i] = 1 if switches[i] == 0 else 0

for i in range(1, len(switches)):
    print(switches[i], end=' ')
    if i % 20 == 0: print()

# 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1