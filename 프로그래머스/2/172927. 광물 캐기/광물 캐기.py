def solution(picks, minerals):
    '''
    5개를 연속해서 캐야함.
    그렇다면 하나라도 다이아몬드가 있으면 다이아
    하나라도 철이 있으면 철
    아니면 돌
    
    minerals에서 5개씩 순서대로 캐야함.
    [다이아, 철, 돌] 0~5 / 6~10 이런식으로 개수를 나눠서 sort
    '''
    rock = []
    p = [0, 0, 0]
    n = min(sum(picks)*5, len(minerals))
    print(n)
    for i in range(n):
        
        if minerals[i] == "diamond":
            p[0] +=1
        elif minerals[i] == "iron":
            p[1] +=1
        else: p[2] +=1

        if (i+1) % 5 == 0: # 5개씩 해야하니까
            rock.append(p)
            p = [0, 0, 0]
                   
                   
    if n % 5 != 0:
        rock.append(p)
    rock.sort(key = lambda x: (-x[0], -x[1], -x[2]))
    rock = rock[::-1]
    ans = 0
    
    # picks가 minerals를 모두 못파면 이후꺼를 빼줘야함.
    # 따라서 앞에서부터 그 개수까지만 추가하기
    while sum(picks) != 0 and rock:
        a, b, c = rock.pop()
        if picks[0] != 0:
            ans += a+b+c
            picks[0]-=1
        elif picks[1] != 0:
            ans += 5*a + b + c
            picks[1]-=1
        else:
            ans += 25*a + 5*b+c
            picks[2]-=1
    
    return ans
        
        
        
    