from collections import deque
import sys
inp = sys.stdin.readline

# 1. stack을 사용하면됨.ㅣ -> deque로 구현
stck = deque()
cur = 0
# 2. n은 사람 수
n = inp().strip() 

# 3. n명이 순서대로 들어옴. + int로 형변환
list = deque(map(int, inp().strip().split()))

# 문제는 1번부터 순서대로 간식을 받을 수 있느냐임.
# 1. 현재 번호가 맞다면 바로 이동
# 2. 현재 번호가 아니라면 대기열 제일 위에 사람 하기
# 3. 만약 대기열 제일 위의 사람도 아니라면 스택에 현재번호 넣어야함.
# 4. -> 이때 현재번호보다 스택의 [-1]이 더 작다면 불가능해서 종료해야함.

while list:
    curCnt = list.popleft()
    if curCnt == cur + 1:
        cur+=1
    else: # 현재 번호가 아님.
        while stck and stck[-1] == cur+1: # 스택에 있는 수들이 계쏙해서 와야할때
            stck.pop()
            cur+=1
        stck.append(curCnt)

while stck:
    curCnt = stck.pop()
    if curCnt == cur + 1:
        cur+=1
    else:
        print("Sad")
        exit()

print("Nice")