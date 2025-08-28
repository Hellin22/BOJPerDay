from collections import defaultdict
def solution(weights):
    '''
    weights의 길이는 2~십만
    2, 3, 4 거리
    
    시소짝꿍 인지 아닌지만...
    
    1. 몇 m에서 되는지는 상관없음
    되는 사람이 있는지만 중요함.
    되기만 한다면 상관 없을거같음.... -> 만약 되는 사람이 있다? 그 사람에 대한 *2, *3, *4를 모두 dt에 추가 -> 이건 불가능한 dt를 의미.
    
    그러면 모든 데이터를 가지고 있는 dt를 만들어야겟네
    여기서 weight에 해당하는(*2, *3, *4)는 -1해주면 될듯
    
    '''
    all_dt = defaultdict(int)
    weight_dt = defaultdict(int)
    for weight in weights:
        weight_dt[weight]+=1
        for i in range(2, 5):
            all_dt[weight*i]+=1
    
        # 현재 값에 대해서  
        
        # key에 대해서 가능한 거리가 있는지 확인
        # for k in all_dt.keys():
            # 이 방법은 사용 불가능. -> 시간초과 뜸
        
        # 같은거는 추가하기 + 배수가 되는거?
        # 2, 3, 4m 니까 하나만 성립됨. 무조건.
    # 2, 3, 4 곱한게 몇개 들어있는가만 찾기
    # 이때 나 포함 동일한게 있을수도 있음. 그때는 weight_dt[현재 weight]*3 빼주면 될듯.
    # *3은 234m니까 
    ans = 0
    for weight in weights:
        for i in range(2, 5):
            ans += all_dt[weight*i]
        ans-=weight_dt[weight]* 2 # 자기자신도 뺴야함.
        ans-=1
        
        
    return ans//2