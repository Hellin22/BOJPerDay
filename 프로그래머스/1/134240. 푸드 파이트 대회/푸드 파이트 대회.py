def solution(food):
    answer = ''
    
    for i, f in enumerate(food):
        # i가 0인거는 제외
        if i == 0: continue
        
        for k in range(f//2):
            answer+=str(i)
            
    answer+=str(0)
    
    for i in range(len(food)-1, -1, -1):
        for k in range(food[i]//2):
            answer+=str(i)
        
        
    return answer