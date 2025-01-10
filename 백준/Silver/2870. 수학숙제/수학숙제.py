import sys

inp = sys.stdin.readline

# print(ord("0")) # 48
# print(ord("9")) # 57
n = int(inp().strip())
llist = [] # 모든 숫자를 저장할 배열

str_list = [inp().strip() for _ in range(n)] 
# n개의 행 -> 각 행은 inp().strip()
# 모든 줄을 돌면서 ord(i)가 0~9 사이의 값인지 확인
# num을 만들고 기존에는 str인데 여기다가 계쏙 하나씩 붙여가면서 진행
plus_str = ""
for i in range(n):
    plus_str = "" # plus_str 초기화 -> llist에 저장하면 다시 str = ""로 초기화 
    for j in range(len(str_list[i])):
        if(48 <= ord(str_list[i][j]) <= 57):
            plus_str += str_list[i][j]
        else:
            if(len(plus_str) != 0):
                llist.append(int(plus_str))
                plus_str = ""
        
        if(j == len(str_list[i])-1):
            if(len(plus_str) != 0):
                llist.append(int(plus_str))

llist.sort()

for i in range(len(llist)):
    print(llist[i])

