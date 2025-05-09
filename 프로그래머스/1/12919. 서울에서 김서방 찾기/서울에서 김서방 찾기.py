def solution(seoul):
    answer = ''
    
    for i, val in enumerate(seoul):
        if val == "Kim":
            return f"김서방은 {i}에 있다"
