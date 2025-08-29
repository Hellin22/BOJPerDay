def solution(orders, course):
    '''
    1. orders[i]들을 모두 sort
    2. course에 있는 숫자만큼 조합 만들기 -> 그후에 dt에 추가하기 (개수)
    '''
    
    # 1. 모두 sort
    for i in range(len(orders)):
        orders[i] = "".join(sorted(orders[i]))
        
    # 2. 조합 만들기 -> itertools? or 조합 메서드
    dt = dict()
    cob = []
    def comb(i, cur, n): # 크기가 n개
        if len(cob) == n:
            dt["".join(cob)] = dt.get("".join(cob), 0)+1
            return
        
        for idx in range(i, len(orders[cur])):
            cob.append(orders[cur][idx])
            comb(idx+1, cur, n)
            cob.pop()
    
    for cs in course:    
        for idx, order in enumerate(orders):
            comb(0, idx, cs)
    
    llist = list(dt.items())
    llist.sort(key = lambda x: (-len(x[0]), -x[1]))
    
    ans = []
    visit = [0] * 11
    for alpa, cnt in llist:
        if cnt == 1: continue
        if visit[len(alpa)] > cnt: continue
        visit[len(alpa)] = cnt
        ans.append(alpa)
    return sorted(ans)