def solution(s):
    answer = 0

    stck = []
    # 결국에 2개씩
    for i in s:
        if stck and stck[-1] == i:
            stck.pop()
        else: stck.append(i)
    
    return answer if stck else 1