def solution(k, m, score):
    answer = 0
    
    # 일단 사과의 수를 sorting 하고
    # m개의 단위로 나눠서 진행
    
    score.sort(key = lambda x: x)
    
    for i in range(len(score)-1, -1, -m):
        if i+1-m < 0: break
        else:
            answer += score[i+1-m] * m
        
    return answer