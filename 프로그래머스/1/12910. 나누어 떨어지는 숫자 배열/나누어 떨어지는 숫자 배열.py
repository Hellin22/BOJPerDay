def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0: answer.append(i)
    answer.sort(key = lambda x: x)
    if answer == []: answer.append(-1)
    return answer