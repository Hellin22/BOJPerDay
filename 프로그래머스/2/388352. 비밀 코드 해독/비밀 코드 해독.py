st = set()
gbn, gbq, gbans = 0, 0, 0
gbanswer = 0
def solution(n, q, ans):
    global gbn, gbq, gbans
    answer = 0
    
    gbn, gbq, gbans = n, q, ans
    
    comb(0, 1, n)
    answer = gbanswer
    return answer

def comb(cnt, cur, n):
    if cnt == 5:
        check()
        return
    
    for i in range(cur, n+1):
        st.add(i)
        comb(cnt+1, i+1, n)
        st.remove(i)

def check():
    global gbanswer, gqb, gqans
    cnt = 0
    for i in range(len(gbq)):
        llist = gbq[i]
        correctCnt = 0
        for j in range(len(llist)):
            if llist[j] in st:
                correctCnt+=1
    
        if correctCnt == gbans[i]: 
            cnt+=1
        else: return
    
    gbanswer+=1