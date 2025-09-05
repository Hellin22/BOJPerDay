def solution(s):
    '''
    완탐을 해야하는가?
    len(s)의 절반까지만 가보기
    앞에서부터 잘라야함.
    "개수" 만큼 짜르는 방법이 있는가?
    아 완전히 개수만큼만 짤라야함.
    idx를 1씩 증가시키는게 아님. -> 공약수만큼 나눠야함.
    '''
    minn = len(s)
    for i in range(1, len(s)//2+1): # 하나의 sttr의 크기
        llist = [] # 개수, sttr
        sttr = ""
        j = 0 # j는 현재 idx
        while j < len(s):
            sttr += s[j]
            if len(sttr) == i:
                if llist and llist[-1][1] == sttr:
                    cnt, ns = llist.pop()
                    llist.append((cnt+1, ns))
                else:
                    llist.append((1, sttr))
                
                sttr = ""
            j+=1
            
        # 마지막 sttr llist에 추가
        if sttr != "":
            llist.append((1, sttr))
        minn = min(minn, sum([len(str(x[0])) + len(x[1]) if x[0] != 1 else len(x[1]) for x in llist ]))
                   
    return minn