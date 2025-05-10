def solution(ingredient):
    answer = 0
    '''
    빵 야채 고기 빵 -> 포장한다.
    스택을 사용해서 풀 수 있겠는가?
    항상 4개의 스택을 살펴봐야한다.
    '''
    stck = []
    
    for v in ingredient:
        if len(stck) >= 3 and stck[-1] == 3 and stck[-2] == 2 and stck[-3] == 1 and v == 1:
            answer += 1
            for i in range(3):
                stck.pop()
        else: stck.append(v)
    return answer