
def solution(word):
    '''
    A E I O U
    
    A AA AAA AAAA AAAAA
    AAAAE AAAAI AAAAO AAAAU
    AAAEA AAAEE ...
    
    어떤 단어가 몇번째인지?
    '''
    llist = ['A','E','I','O','U']
    # 0 1 2 3 4
    # 0
    # 00 000 0000 00000 -> len(str)이 5이면 더이상 추가 못하니까 종료조건이면 더이상 추가 못하니까 종료조건
    ans = ""
    cnt = 0
    flg = False
    def dfs():
        nonlocal word, ans, cnt, flg
        if ans == word: # 만약에 둘이 같다면
            flg = True
            return
        
        if flg == True: return
        
        cnt+=1
    
        # 1. 만약 길이가 5이다? 너 못늘리기 때문에 pop
        if len (ans) == 5: 
            return
        # 2. 만약 길이가 5가 아니다? for문 돌리기 -> 그 안에서 +=하기
        else:
            for i in llist:
                ans = ans + i # ans 갱신하기
                dfs()
                ans = ans [:-1] # 반복하고 나서는 제일 뒤에꺼 빼주기
    
    dfs()
    return cnt