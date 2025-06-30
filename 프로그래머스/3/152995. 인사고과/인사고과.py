'''
사원마다 근무태도점수, 동료평가점수

만약 두 점수 모두 임의의 다른 사람보다 낮다? 그러면 인센티브 X

그렇지 않은 사람들은 모두 인센티브를 받는데 두 점수의 합(SUM)으로 석차 매김
동점은 동일한 순위

socres[0]는 완호꺼.
총 십만개

리턴값은 완호의 석차
불가능? -> -1 리턴

완호보다 큰 점수가 몇개있는지 세면됨.
1. 인센티브 못받는놈 모두 제외하기
2. 완호가 못받는지 확인하기
3. 두 점수가 모두 낮은 경우에 못받는거.
'''

def solution(scores):
    answer = 0
    n = len(scores)
    for i in range(n):
        scores[i] = [scores[i][0], scores[i][1], i, 1] # idx -> 완호의 idx는 0임.
    
    scores.sort(key = lambda x: (x[0], x[1]))
    
    
    lmax = scores[-1][1]
    l = scores[-1][0]
    for i in range(len(scores)-1, -1, -1):
        if scores[i][1] > lmax:
            lmax = scores[i][1]
            l = scores[i][0]
        elif scores[i][1] < lmax and scores[i][0] < l:
            scores[i][3] = 0 # 이거는 사용 불가
    
    
    n_scores = []
    for i in range(n):
        if scores[i][3] == 0: continue # 만약 0이라면 추가x 
        n_scores.append(scores[i])
    
    # n_scores는 오른쪽껄로 소팅
    n_scores.sort(key = lambda x: (x[1], x[0]))
    
    rmax = n_scores[-1][0]
    r = n_scores[-1][1]
    for i in range(len(n_scores)-1, -1, -1):
        if n_scores[i][0] > rmax:
            rmax = n_scores[i][0]
            r = n_scores[i][1]
        elif n_scores[i][0] < rmax and n_scores[i][1] < r:
            n_scores[i][3] = 0 # 이거는 사용 불가
    
    
    nn_scores = []
    wanho = 0
    wanho_sc = 0
    for i in range(len(n_scores)):
        if n_scores[i][3] == 0: continue # 만약 0이라면 추가x 
        if n_scores[i][2] == 0: # 완호
            wanho = 1
            wanho_sc = n_scores[i][0] + n_scores[i][1]
        nn_scores.append([n_scores[i][0] + n_scores[i][1], n_scores[i][2]])
        
    if wanho == 0: return -1 # 완호는 인센 못받음
    
    nn_scores.sort(key = lambda x: (-x[0], x[1])) # 점수가 큰사람 앞에, idx 작은거
    # 완호의 점수가 처음 나오는 idx 찾기
    for i in range(len(nn_scores)):
        if nn_scores[i][0] == wanho_sc:
            return i+1
    
    return answer