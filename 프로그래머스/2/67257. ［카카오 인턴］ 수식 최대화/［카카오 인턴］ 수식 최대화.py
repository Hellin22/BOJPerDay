'''
연산자 우선순위 적용하기
음수나오면 절대값
+ - *만 주어짐

'''
from copy import deepcopy
from collections import deque
def solution(expression):
    answer = 0
    
    idx = 0
    i = 0
    number_list = []
    char_list = []
    
    r_number_list = []
    r_char_list = []
    while True:
        if i == len(expression): break
        
        if expression[i].isdigit():
            idx = i+1
            while True:
                if idx == len(expression): 
                    break
                if expression[idx].isdigit():
                    idx+=1
                else: break
            number_list.append(int(expression[i:idx]))
            i = idx
            
        else: # i가 문자임
            char_list.append(expression[i])
            i+=1
    print(number_list)
    print(char_list)
    real_number_list = deepcopy(number_list)
    real_char_list = deepcopy(char_list)
    
    cur_pri_ch = []
    ch_dt = {
        0 : "*", 1: "+", 2: "-"
    }
    visit = [0] * 3
    
    def gyesan():
        nonlocal number_list, char_list
        number_list = deepcopy(real_number_list)
        char_list = deepcopy(real_char_list)
        
        print("gyesan 시작", number_list)
        
        cur = 0 # 현재 우선순위 의미 -> cur_pri_ch[cur]
        while len(number_list) != 1:
            # 1개의 숫자만 남는게 아니라면

            stck = []

            # 처음꺼를 먼저 넣기
            stck.append(number_list[0])

            for i in range(1, len(number_list)):
                # 먼저 char_list 확인하기
                if char_list[i-1] == cur_pri_ch[cur]:
                    # 우선순위임.
                    num = stck.pop()

                    if cur_pri_ch[cur] == "+":
                        stck.append(num + number_list[i])
                        # stck에 다시 넣어주기

                    elif cur_pri_ch[cur] == "-":
                        stck.append(num - number_list[i])

                    else:
                        stck.append(num * number_list[i])

                else: # 우선순위가 아니면 그냥 넣기
                    stck.append(char_list[i-1])
                    stck.append(number_list[i])


            cur+=1 # 연산자 우선순위 증가

            print("!@3", stck)

            number_list = []
            char_list = []
            number_list.append(stck[0]) # 처음 숫자 추가

            for i in range(1, len(stck), 2):
                char_list.append(stck[i])
                number_list.append(stck[i+1])

            print(number_list)
            print(char_list)
        return number_list[0]
    
    
    
    
    def perm():
        nonlocal answer
        if len(cur_pri_ch) == 3:
            answer = max(answer, abs(gyesan()))
            return
        
        for i in range(3):
            if visit[i] == 0:
                cur_pri_ch.append(ch_dt[i])
                visit[i] = 1
                perm()
                cur_pri_ch.pop()
                visit[i] = 0
                
    perm()
    
    return answer