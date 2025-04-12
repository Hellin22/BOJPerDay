def solution(picks, minerals):
    answer = 0
    
    mineral_list = [0] * 3
    ml = []
    for i in range(len(minerals)):
        if sum(picks)*5 == i: break
        
        if sum(mineral_list) == 5:
            # 처리 진행
            ml_s = mineral_list[:]
            ml.append(ml_s)
            mineral_list = [0]*3
            
        if minerals[i] == "diamond":
            mineral_list[0]+=1
        elif minerals[i] == "iron":
            mineral_list[1]+=1
        else: mineral_list[2]+=1
        
    if mineral_list[0] != 0 or mineral_list[1] != 0 or mineral_list[2] != 0: # 하나라도 0이 아니라면
        ml.append(mineral_list)
    
    
    ml.sort(key = lambda x: (-x[0], -x[1], -x[2]))
    print(ml)
    
    for dia, iron, rock in ml:
        print(picks)
        if picks[0] != 0:
            answer+= dia+iron+rock
            picks[0]-=1
        elif picks[1] != 0:
            answer += dia*5+iron+rock
            picks[1]-=1
        elif picks[2] != 0:
            answer+=dia*25 + iron*5 + rock
            picks[2]-=1
    
    
    
    return answer

# 다이아가 하나라도 있다면 다이아가 좋음
# 철이 하나라도 있다면 철이 좋음
# 나머지는 돌멩이