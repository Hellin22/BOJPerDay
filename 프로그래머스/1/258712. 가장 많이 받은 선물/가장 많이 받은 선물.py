'''
다음달에 누가 선물을 많이 받을지?

# 1.
a, b -> 두사람 사이에 더 많은 선물 준 사람이 다음달에 선물받음
a->b 5번 b->a 3번 == a가 b에게 선물 하나 받음

# 2. 
안주고받음 or 주고받은 수가 같다면
선물 지수가 큰사람이 작은사람에게 선물 하나 받음

선물지수 = 내가 선물준 수 - 받은선물 수 (- 가능)

if 선물지수도 같다 == 선물 안 주고 받음

'''


def solution(friends, gifts):
    answer = 0
    
    # dict로 치환하는거 필요
    # 친구들의 수는 최대 50 -> 50*50 배열 만듦
    # 51*51? -> [a][50] = a가 준 선물 수
    # [50][a] = a가 받은 선물 수
    
    # a -> b라면 (선물 준놈, 선물 받은놈) [a][b] == a가 b에게 선물 준것
    cnt = len(friends)
    d = {fri:i for i, fri in enumerate(friends)}
    arr = [[0] * (cnt+1) for _ in range(cnt+1)]
    for i in gifts:
        a, b = i.split(" ")
        arr[d[a]][d[b]] +=1
        arr[d[a]][-1] += 1 # a가 준 선물 개수
        arr[-1][d[b]] += 1 # b가 받은 선물 개수
    
    jisu = [0] * cnt # 선물지수 저장
    for i in range(cnt): # 선물지수 계산 -> 준 선물 수 - 받은 선물 수
        jisu[i] = arr[i][-1] - arr[-1][i]
    
    gift = [0] * cnt # 받을 선물 개수 저장
    
    # 모든 사람들에 대해서 계산?
    for i in range(cnt):
        for j in range(i+1, cnt):
            # 내가 더 많이 줬다면 [i][j] > [j][i]라면 ㅇㅋ
            
            if arr[i][j] > arr[j][i]:
                # i j가 더 많이 줬다면
                gift[i]+=1
            elif arr[j][i] > arr[i][j]:
                gift[j]+=1
            else:
                if jisu[i] == jisu[j]: continue
                elif jisu[i] > jisu[j]: # i가 지수 더 큼
                    gift[i]+=1
                
                else: gift[j]+=1
    
    
    return max(gift)









