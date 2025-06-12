'''
판매원	판매 수량	이익금
young	12	1,200 원
john	4	400 원
tod	    2	200 원
emily	5	500 원
mary	10	1,000 원

최악의 경우 선형 -> n^2 == 10000*10000 = 100,000,000 -> 시간초과
그래도 일단 dfs를 해볼까?
그리고 node 개수가 아니라 seller의 개수로 처리해야함.
-> seller는 100,000 -> 다른 방법 찾기

가면 갈수록 10^-1이 곱해짐. -> (10, 6)?

set을 사용하기?
합집합 사용하면 바로바로 구할 수 있지 않나? ^인가? |인가 &는 교집합 / |가 합집합

amount의 크기는 최대 100임 -> 칫솔 하나는 100원
즉, 최대 100,000원임.
10^-1씩 계속해서 줄어듦. 따라서 최대 끝까지 올라가는게 아니라 
100,000 a
10,000 b
1,000 c
100 d
10 e
1 f -> 여기 위로는 올라가지 않음.
즉, 최대 5명의 상위한테 가기 때문에 시간복잡도에 걸리지는 않을거라고 생각
1. enroll, referral를 보고 그래프 구성하기 (그래프 숫자로 구성하는게 좋을거같음.)
2. seller에 대해서 가격 분배하기
'''

def solution(enroll, referral, seller, amount):
    answer = []
    
    # enroll 기준. 부모가 없다는 의미. 만약 '-'이면 center가 부모인 것.
    # 즉, referral -> enroll로 연결된다고 생각하면 된다.
    # 먼저 모든 사람을 dt에다가 번호로 저장하고 생각하기
    
    dt = dict()
    dt_rev = dict()
    dt_rev[0] = "center"
    dt["center"] = 0 # 최상단 root 저장
    for i, name in enumerate(enroll):
        dt[name] = i+1 # root 제외하고 1번부터 저장
        dt_rev[i+1] = name
    
    arr = [-1] * (len(enroll)+1) # 0번 부터 쭉 저장
    
    for to, fr in zip(referral, enroll):
        # 결국 부모만 누군지 알면 됨. -> 역방향 트리라 생각하면 됨. 1:1 관계 유지
        if to == "-": to = "center"
        
        # 배열의 idx라 문자로 저장 불가능
        arr[dt[fr]]= dt[to]
        
    earn = [0] * (len(enroll)+1)
    
    def dfs(number, money): # 번호, 금액
        if money < 10: 
            # 추가하고 리턴
            earn[number] += money    
            return
        
        if arr[number] == -1:
            # 이어있지 않다?
            earn[number] += money
            return
        
        earn[number] += money-money//10
        dfs(arr[number], money//10)
        
        
    # 가격 계산하기
    for i, name in enumerate(seller):
        # 일단 더하고 10% 계산해서 빼주고 dfs 호출하기?
        
        dfs(dt[name], amount[i] * 100)

    for val in enroll:
        answer.append(earn[dt[val]])
    
    return answer