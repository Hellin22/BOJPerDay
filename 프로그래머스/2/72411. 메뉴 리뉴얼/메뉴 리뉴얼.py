'''
단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공
어떤 단품메뉴들을 조합?
가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함

set으로 진행? issubset 메서드를 사용?
orders ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"] 20개 -> 각각은 크기 10
course [2,3,4] -> course는 뭐임? 2개 단품 묶음 + 3개 단품 + 4개 단품을 코스로 만들고싶음
10개
-> 배달 되는거는 순서 상관 x -> set에다가 저장
완탐으로 푼다고 하면?
orders의 크기는 최대 10개임
모든 가능한것 = 최대 1개는 가지고 있어야 하니깐
cur_str = ""
for i in range(idx): idx+1부터 진행.
    str += orders[k][idx] -> stttr = str[::-1] # 뒤집은거도 넣어야 하기 때문
    set에다가 집어넣기
    str += orders[k][idx]

그래서 몇번 하는건데?
최대 10개를 가지고 있고 길이는 20개임.
거꾸로 해야하니까 2곱하기 -> 10번 조합에 대해서 40 곱하기
2개부터 해야하는거 잊지말기 -> 그리고 사전순으로 해야함. 즉, sort를 계속 걸어버리면 상관없음
그렇게 따지면 처음부터 orders에 대해서 모두 sort 걸어버리면 되겠네?
이거 시간 측정을 못하겠네
10c2 + 10c3 + ... + 10c10
10c5  3 2 7 6 /     1 -> 무조건 됨.

정리하면
1. orders[i]를 모두 sort 하기 -> 문자열 sort? -> list로 바꿔서 sorting 해버리기?
 -> 문자열 sort()는 없음. -> sorted를 적용해서 list 반환 후 "".join 적용하기
2. 크기 11 배열 만들어가지고 course만큼 돌면서 arr[course[i]] = 1로 만들기 (크기가 course[i]인 경우에 set에다 추가)
 -> set이 아니라 dict로 진행? why? -> 똑같은 메뉴 구성이 여러개 있어도 1만 check 해야함(마지막에는 key 돌면서 추가하면됨)
    크기 11 배열은 ssize
3. dfs 메서드 진행 (dict도 만들기)
'''

def solution(orders, courses):
    answer = []
    ssize = [0] * 11
    dt = dict()
    # 1.
    for i, order in enumerate(orders): 
        order = sorted(order)
        order = "".join(order)
        orders[i] = order
    # 2.
    for course in courses:
        ssize[course] = 1
    
    sttr = ""
    # 3. 
    def dfs(idx, orderLen, orderIdx): # 현재 str의 크기 저장할 전역 변수 있어야함.
        nonlocal sttr
        
        for i in range(idx, orderLen): # 어디까지 해야함? orders의 번호의 크기만큼 == len(orders[i]) -> 그리고 orders의 몇번째인지 알아야함
            sttr+=orders[orderIdx][i]
            # print(sttr, orderIdx)
            if ssize[len(sttr)] == 1:
                dt[sttr] = dt.get(sttr, 0) + 1
            dfs(i+1, orderLen, orderIdx)
            sttr = sttr[0:-1]
            
    
    for i, order in enumerate(orders):    
        dfs(0, len(order), i)
    # print(dt)
    # for key, val in dt.items():
        # print(key if val > 1 else 0) # 아 그거중 가장 많은거를 반환해야하네
    arr = [[] for _ in range(11)] # 
    
    for key, val in dt.items():
        if val > 1:
            arr[len(key)].append((-val, key)) # 어떤걸 넣을까 (개수하고 key)
    
    for i in range(1, 11):
        arr[i].sort()
    # print(arr)
    
    for i in range(1, 11):
        maxx = 0
        for cnt, val in arr[i]:
            cnt*=-1
            if maxx == 0:
                maxx = cnt
                answer.append(val)
            elif maxx == cnt:
                answer.append(val)
            else: break
    
    answer.sort()
    # print(answer)
    
    
    return answer