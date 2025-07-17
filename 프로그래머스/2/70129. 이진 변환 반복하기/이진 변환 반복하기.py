def solution(s):
    z_cnt = 0
    cnt = 0
    # 1. 모든 0 제거하기
    # 2. x의 길이 c를 다시 2진법으로 바꾸기
    # 3. 0의 개수 + 몇번 반복했는지 저장 
    
    while s != "1":
        z_cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt+=1        
    return [cnt, z_cnt]