'''
gems를 모두 보면서 새로운 보석이 있다면 -> set에 없다면 추가해줘야함.
이걸 set, dict 말고 좀더 쉽게 할 수 있는 방법이 있는가?
dict 하나로도 할 수 있지 않나?
defaultdict를 한번 써보자!

'''
def solution(gems):
    left, right = 0, 0
    dt = dict()
    cur_dt = dict()
    for gem in gems:
        dt[gem] = dt.get(gem, 0) + 1
    
    n = len(dt.keys())
    ans_left, ans_right = 0, 10000000
    cnt = 1
    cur_dt[gems[0]] = cur_dt.get(gems[0], 0)+1
    # 조건을 딱 정하기
    # 0. left, right를 다 처리하고 마지막에 dt에 추가하든 빼든 진행
    # 1. 만약 cnt가 n과 같다 
    # => left 갱신(일단 하나씩으로 진행 while left가 아님) 
    #    마지막에 dt에서 빼주기 + 만약 dt에서 뺐는데 0이되면 del 진행 + cnt -1
    #    만약 cnt과 n과 같은데 right = left다? 그러면 right를 하나 늘려주기
    # 
    # 2. 만약 cnt가 n과 다르다
    # 무조건 right를 하나 늘려주기
    while left != len(gems):
        if cnt == n:
            # 만약 cnt == n이라면 ans_right, ans_left를 갱신해주기
            if ans_right - ans_left > right - left:
                ans_right, ans_left = right, left
            
            if right != left: # left를 오른쪽으로 한칸 땡기면 됨.
                if cur_dt[gems[left]] == 1:
                    del cur_dt[gems[left]]
                    cnt-=1
                else: cur_dt[gems[left]] -= 1
                left+=1
            else: # 2개가 동일하면 right를 오른쪽으로 한칸 댕기기
                right+=1
                if right == len(gems): break # 만약 right가 gems 개수가 되면 종료
                
                cur_dt[gems[right]] = cur_dt.get(gems[right], 0) + 1
                cnt = len(cur_dt)
        else: # cnt != n인 경우 -> right를 늘려줘야함.
            right+=1
            if right == len(gems): break
            cur_dt[gems[right]] = cur_dt.get(gems[right], 0) + 1
            cnt = len(cur_dt)
        
    # print(ans_right, ans_left)
    return [ans_left+1, ans_right+1]