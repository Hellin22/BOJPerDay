from collections import defaultdict
def solution(str1, str2):
    answer = 0
    
    '''
    str1, str2
    자카드 유사도 적용
    교집합 크기를 합집합으로 나눈 값.
    
    a, b가 공집합이면 1로 정의
    65536 곱하고 정수부만
    두 글자씩 끊어서 다중집합 원소로
    -> 문자만 적용하기
    
    중복이 적용됨. -> dt로 바꿔서 해보기.
    '''
    
    str1, str2 = str1.upper(), str2.upper()
    dt1, dt2 = defaultdict(int), defaultdict(int)
    
    for i in range(len(str1)-1):
        ss = str1[i:i+2]
        if ss.isalpha():
            dt1[ss]+=1
    for i in range(len(str2)-1):
        ss = str2[i:i+2]
        if ss.isalpha():
            dt2[ss]+=1
    
    
    gyo, hab = 0, 0
    
    # 이제 중복되는거 찾기
    # 1. dt1 기준 dt2에 있는거 찾기 -> 교집합 -> 교집합 = 둘 모두에 있는거 기준.
    # 1-2. d1에 있고 d2에 있다? 그러면 min값을 가져오기
    for k in dt1:
        if k in dt2: # dt1의 key값이 dt2에 있다?
            gyo+=min(dt1[k], dt2[k])
            hab+=max(dt1[k], dt2[k]) # 합집합
        else: # 합집합
            hab+=dt1[k]
        
    # 2. 합집합 = dt1의 모든것 + dt2 -> dt1의 모든 개수 + dt2에만 있는것 -> dt2를 돌면서 dt1에 있는지 없는지 확인
    for k in dt2:
        if k not in dt1:
            hab += dt2[k]
            
    if hab == 0: return 65536
    else: return gyo * 65536 // hab