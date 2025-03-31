'''
numbers에서 numbers[i]보다 뒤에 있으면서 큰 수를 answer.append 하면됨
만약 없다? -1을 넣기
len(numbers)는 최대 백만 -> 하나씪 다 보면서 최대값을 보는건 의미 없음
뒤에서부터 보면서 -> 자신보다 크기만하면 됨. + 가장 가까이에 있어야함
내림차순배열? -> n2이 됨.
stack 사용?
1. -1번째 stck에 집어넣고 -1로 바꿈
2. 뒤에서부터 오면서 if stck[-1]이 현재보다 크다? 그러면 그거 적용후 자신도 집어넣기
elif stck[-1]이 현재보다 작거나 같다? 그러면 큰수가 아니니까 top 빼야함.
언제까지? top이 뒷큰수일때 or stck이 빌때까지
'''
def solution(numbers):
    answer = []
    
    next_bigger_nums = [] # ㅁ마지막에 뒤집기
    stck = []
    stck.append(numbers[-1]) # 원소값 넣기 -> numbers[i]
    next_bigger_nums.append(-1)
    
    for i in range(len(numbers)-2, -1, -1):
        if stck and stck[-1] > numbers[i]:
            next_bigger_nums.append(stck[-1])
            stck.append(numbers[i])
        else:
            while True:
                if not stck: 
                    # stck이 빈다면 -1임 + 내꺼넣기    
                    next_bigger_nums.append(-1)
                    stck.append(numbers[i])
                    break
                elif stck:
                    if stck[-1] <= numbers[i]: # 빼야함.
                        stck.pop()
                    elif stck[-1] > numbers[i]: # 이거임.
                        next_bigger_nums.append(stck[-1])
                        stck.append(numbers[i])
                        break
    return next_bigger_nums[::-1]
    
