def solution(s):
    n = len(s)
    ans = 0
    
    for i in range(n):
        # 시작점
        srt = i-1
        flg = True
        stck = []
        for j in range(n):
            srt = (srt+1) % n
            
            if( stck and
                ((stck[-1] == '(' and s[srt] == ')') or
                (stck[-1] == '[' and s[srt] == ']') or
                (stck[-1] == '{' and s[srt] == '}'))):
                stck.pop()
            elif s[srt] == '(' or s[srt] == '[' or s[srt] == '{':
                stck.append(s[srt])
            else: 
                flg = False
                break
            
        if not stck and flg == True: ans+=1
    return ans


    '''
    왼쪽으로 x칸 만큼 회전 -> s가 올바른가?
    x칸은 0~s-1 만큼 회전한것
    스택 말고 a1, a2, b1, b2, c1, c2로 하기
    
    -> 중첩구조를 파악못해서 이걸로 못품
    ([)] -> 이것도 맞는거처리되기 때문
    
    
    
    '''