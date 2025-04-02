'''
전대회 우승자는 불리함.
n은 최대 10임
어피치의 화살 맞추는 횟수는 알고있음7.
완탐이 가능한가? n발
11개의 자리가 있음. 그중 n개를 선택 -> 중복되도 되는가?> 됨. 순열인가? 아님.
즉, 중복 조합이라는 의미. idx부터. 즉, idx+1이 아닌 자신도 포함해서 적용 가능하게 한다.
가장 낮은 점수를 많이 가져간것 중에서 가장 큰 점수차이를 구해야함.
1. 중복 조합을 통해서 나올 수 있는 경우의 수를 구함.
2. 어피치 과녁과 비교해서 둘의 점수를 구함.
 2.1 만약 라이언이 더 크다. -> res와 비교 -> 현재 > res라면 answer = 라이언[]
                                        else라면 아무것도 안함.
 2.2 만약 라이언이 더 작다. -> 아무것도 안함.
'''
def solution(n, info):
    info = info[::-1]
    
    score_diff = -1 # 라이언이 더 크게 이길 수 있는 점수(max)
    # 여기서 점수차이가 커야 이기는거임. 라이언 점수가 많다고 무조건 교체는 아님
    score_answer = [-1] # 정답
    lion = [0] * 11
    # lion = [] # 라이언이 과녁 맞춘 개수 (0점부터임.)
    # -> 즉, info[0]는 어피치가 0점 맞춘 개수, lion[0]는 라이언이 0점 맞춘 개수
    def duplicate_comb(idx, cur_n):
        nonlocal n
        if cur_n == n:
            check()
            return
        
        for i in range(idx, 11): # idx부터 11까지
            lion[i]+=1
            duplicate_comb(i, cur_n+1)
            lion[i]-=1
    
    def check():
        nonlocal score_diff, score_answer, n
        # lion과 info를 본다.
        l_score, info_score = 0, 0
        for i in range(len(info)):
            if lion[i] > info[i]: # lion이 더 크다? l_score에 i 더하기
                l_score+=i
            elif lion[i] < info[i]: # info가 더 크거나 같다.
                info_score+=i
            elif lion[i] == info[i] and info[i] != 0:
                info_score+=i
        if l_score > info_score: # lion이 우승
            if score_diff < (l_score - info_score):
                score_diff = l_score-info_score
                score_answer = lion[:]
            elif score_diff == (l_score - info_score):
                # 동일하다면 낮은 점수가 많은거를 가져와야함.
                for i in range(len(info)):
                    if lion[i] > score_answer[i]:
                        score_answer = lion[:]
                        break
                    if score_answer[i] > lion[i]:
                        break
    duplicate_comb(0,0)
    
    return score_answer[::-1]