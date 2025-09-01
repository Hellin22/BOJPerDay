from itertools import permutations
from collections import deque
def solution(expression):
    '''
    숫자는 0~999사이 숫자.
    어떤 우선순위로 하든간에 그걸 어떻게 순서 정해주더라?
    길이 100이하 문자열
    3번 반복하면서 해당하는 연산자가 있으면 적용하기?
    가능할거 같기는 함.
    
    '''
    maxx = -987654321
    operator_list = list(permutations(["*", "-", "+"], 3))
    exp = expression
    for operator in operator_list:
        expression = exp
        for op in operator: # '*', '+', '-'

            stck = []
            new_str = ""
            if op == "*": # expression에 대해서 *만 찾아서 진행.
                i, j = 0, 1
                while i < len(expression) and j < len(expression):
                    if expression[j] not in ("*", "+", "-"):
                        j+=1
                    else: 
                        # 연산자가 나오면 expression[i:j]는 하나의 숫자를 의미
                        # 만약 stck[-1]이 우선순위에 있는 연산자라면 연산후 집어넣기
                        if stck and stck[-1] == "*":
                            stck.pop()
                            num = stck.pop()
                            stck.append(num * int(expression[i:j]))
                            stck.append(expression[j])
                        else:
                            stck.append(int(expression[i:j]))
                            stck.append(expression[j])
                        i = j+1
                        j = i+1

                if stck and stck[-1] == "*":
                    stck.pop()
                    num = stck.pop()
                    stck.append(int(expression[i:]) * num)

                else: # 마지막 숫자 집어넣기
                    stck.append(expression[i:])

            elif op == "+": # expression에 대해서 *만 찾아서 진행.
                i, j = 0, 1
                while i < len(expression) and j < len(expression):
                    if expression[j] not in ("*", "+", "-"):
                        j+=1
                    else: 
                        # 연산자가 나오면 expression[i:j]는 하나의 숫자를 의미
                        # 만약 stck[-1]이 우선순위에 있는 연산자라면 연산후 집어넣기
                        if stck and stck[-1] == "+":
                            stck.pop()
                            num = stck.pop()
                            stck.append(num + int(expression[i:j]))
                            stck.append(expression[j])
                        else:
                            stck.append(int(expression[i:j]))
                            stck.append(expression[j])
                        i = j+1
                        j = i+1

                if stck and stck[-1] == "+":
                    stck.pop()
                    num = stck.pop()
                    stck.append(int(expression[i:]) + num)

                else: # 마지막 숫자 집어넣기
                    stck.append(expression[i:])

            elif op == "-": # expression에 대해서 *만 찾아서 진행.
                i, j = 0, 1
                while i < len(expression) and j < len(expression):
                    if expression[j] not in ("*", "+", "-"):
                        j+=1
                    else: 
                        # 연산자가 나오면 expression[i:j]는 하나의 숫자를 의미
                        # 만약 stck[-1]이 우선순위에 있는 연산자라면 연산후 집어넣기
                        if stck and stck[-1] == "-":
                            stck.pop()
                            num = stck.pop()
                            stck.append(num - int(expression[i:j]))
                            stck.append(expression[j])
                        else: # "+", "-"
                            stck.append(int(expression[i:j]))
                            stck.append(expression[j])
                        i = j+1
                        j = i+1

                if stck and stck[-1] == "-":
                    stck.pop()
                    num = stck.pop()
                    stck.append(num - int(expression[i:]))

                else: # 마지막 숫자 집어넣기
                    stck.append(expression[i:])

            for i in stck:
                new_str += str(i)
            expression = new_str

        maxx = max(maxx, abs(int(expression)))
    return maxx