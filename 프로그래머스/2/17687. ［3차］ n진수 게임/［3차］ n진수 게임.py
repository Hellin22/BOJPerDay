'''
n은 몇진법인지
t는 미리 구할 숫자 갯수(1~1000) -> 내가 말해야하는 숫자
m은 참가하는 사람수 (2~100)
p는 내 순서 (p는 1~m 이겠죠)

완탐으로 진행?
n 진법만큼 idx에 수가 올 수 있음

완탐 진행해보기

'''

from collections import deque
def solution(n, t, m, p):
    answer = []
    
    def nzinbub(n, num):
        res = deque()
        while num//n != 0: # 몫이 0이 아니라면 계속해서 나눠지는것
            res.appendleft(num%n)
            num = num//n
        res.appendleft(num%n)
        return list(res)
    
    cur = 0 # cur이 t개가 된다면 종료
    num = 0
    cur_p = 0 # 현재 순서
    # p가 순서임. -> 현재 순서 cur_p %= m으로 진행
    while cur != t:
        llist = nzinbub(n, num)
        for i in range(len(llist)):
            if cur_p == p-1: 
                answer.append(llist[i])
                cur+=1
                if cur == t: break
            cur_p = (cur_p+1) % (m)
        
        num+=1
    for i in range(len(answer)):
        if answer[i] == 10: answer[i] = "A"
        if answer[i] == 11: answer[i] = "B"
        if answer[i] == 12: answer[i] = "C"
        if answer[i] == 13: answer[i] = "D"
        if answer[i] == 14: answer[i] = "E"
        if answer[i] == 15: answer[i] = "F"
    
    return "".join(map(str, answer))
