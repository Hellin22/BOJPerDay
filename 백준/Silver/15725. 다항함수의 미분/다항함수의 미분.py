import sys
from collections import deque

inp = sys.stdin.readline

sig = inp().strip()
stck = deque()
res = 0
# x가 나오면 stack에서 빼자!!
# 계수가 +1이면 계수가 안보이니까 x가 나왔는데 stck이 비어있으면 1로 처리하면 될듯?
for i in range(len(sig)):
    if sig[i] == 'x':
        if len(stck) == 0: # 1번만 적용 + x가 나왔는데 스택이 비어있음 == 1 
            res+=1
        else:
            stckStr = ''.join(stck)
            if stckStr == '-': res -= 1                
            else: res+=int(stckStr)
            stck.clear()

    else:
        stck.append(sig[i])

print(res)