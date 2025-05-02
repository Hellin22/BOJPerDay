def solution(absolutes, signs):
    answer = 0
    
    for i, num in enumerate(absolutes):
        answer = answer + num if signs[i] == True else answer - num
        
        
    
    return answer