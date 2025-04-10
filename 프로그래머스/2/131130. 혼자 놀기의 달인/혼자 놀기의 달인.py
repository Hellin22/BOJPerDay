'''
숫자 하나 선택 -> 그 숫자 이하의 숫자카드 + 카드수만큼 상자 준비
[8,6,3,7,2,5,1,4]	12


# 모든 상자에 대해서 진행
# 어짜피 2개의 그룹만 만들면 성공
# visit 한거는 다시 가면 안됨.
# 대표그룹 dt로 진행?
# 상자수를 기준으로 진행함. -> 노상관이지 않나 그러면?
'''
# 이거는 완탐 해야하는거같은데 굳이 시간복잡도 안줄여도 될거같음.
# 처음에 어떤걸 뽑았을때 
    

def solution(cards):
    cards = [0] + cards
    answer = 0
    
    visit = [0] * (len(cards))
    box_count = [0] * (len(cards))
    
    def open_box1(idx):
        # 첫번째 그룹 체크
        # idx에 대해서 연쇄적으로 상자 열기
        if visit[cards[idx]] != 0:
            return visit.count(1) # 선택된 (1인) 개수 세기
        else:
            visit[cards[idx]] = 1
            return open_box1(cards[idx])
        
        
    # def open_box2(idx):
        # 두번째 그룹 체크
        
    maxx = 0
    for i in range(1, len(cards)):
        # i가 1번인 상자부터 열 예정임
        visit = [0] * (len(cards))
        visit[i] = 1

        a = open_box1(i)
        vvv = visit[:]
        for j in range(1, len(cards)):
            if visit[j] == 0:
                b = open_box1(j)
                maxx = max(a*(b-a), maxx)
            visit = vvv[:]    
    return maxx

