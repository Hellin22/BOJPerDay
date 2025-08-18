from collections import defaultdict
def solution(topping):
    
    '''
    토핑 종류에 관심.
    2개로 잘랏을때 토핑 개수가 같으면 굿
    
    
    '''
    
    ans = 0
    i = 0
    dt1, dt2 = defaultdict(int), defaultdict(int)
    for k in topping[1:]:
        dt2[k]+=1
    dt1[topping[i]] +=1
    while i != len(topping)-1:
        if len(dt1) == len(dt2):
            ans+=1
        i+=1
        
        dt2[topping[i]]-=1
        if dt2[topping[i]] == 0:
            del dt2[topping[i]]
        
        dt1[topping[i]]+=1
        
    return ans