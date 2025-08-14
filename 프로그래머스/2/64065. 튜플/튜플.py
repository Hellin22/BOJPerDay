def solution(s):
    answer = []
    
    i = 2
    ans = []
    cnt = 0
    while i < len(s):
        cnt+=1
        j = i
        cur_arr = []
        while s[i] != '}': # i가 }를 만날때 까지
            i+=1
        
        sttr = s[j:i]
        llist = sttr.split(',')
        ans.append(llist)
        
        i+=3
        
        if i >= len(s)-2: break
    
    ans.sort(key = lambda x: len(x))
    st = set()
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if ans[i][j] not in st:
                answer.append(int(ans[i][j]))
                st.add(ans[i][j])
                break
    return answer

    '''
    1. 짧은 순서로 정렬한 후에 result에 아직 없는거 추가해주기 (1개씩 추가하면 됨)
    -> 정렬을 어떻게 할 것인가?
    '''
    
    
    return answer