'''
필요한것 
1. 어디서부터 문자열을 만들것인지 idx
2. 지역변수 idx_j -> idx ~ idx_j-1까지가 색인에 포함되는지.
3. 색인을 저장하고있을 set과 dict -> dict만 다루면 색인에 존재하는지 확인하는데 시간 걸림 
-> st ("SA") / dt ("SA": 2)
4. 색인 저장할 배열 (answer)
5. 색인 번호(27부터 저장해야함.) -> saegin
'''
def solution(msg):
    cnt = 0
    answer = []
    idx = 0
    saegin = 27
    st = set()
    dt = dict()
    for i in range(1, 27): # 최초 색인 초기화
        dt[chr(i+64)] = i
    while idx != len(msg): # cur이 msg 범위 벗어나는 순간 종료
    # while cnt != 5:
        sttr = msg[idx]
        # print(sttr)
        # if sttr in dt: # 만약에 색인에 존재하는 단어였다면? 색인에 존재하지 않을때까지 반복
        # 단어 하나만 보는데 색인에 없을수가 없음   
        new_str = sttr
        flag = False # 만약 추가했으면 True로 바뀜. -> False라는 의미는 새롭게 추가할 필요 없는것.
        for idx_j in range(idx+1, len(msg)):
            new_str = new_str + msg[idx_j]
            if new_str in st: # 만약 st에 아직도 존재한다? 그대로 진행                    
                continue
            else: # dt에 없다? 색인에 추가해야함
                dt[new_str] = saegin
                st.add(new_str)
                saegin+=1
                answer.append(dt[new_str[:-1]])
                idx = idx_j
                flag = True
                break 
        if not flag:
            answer.append(dt[new_str])
            idx = len(msg)
            break
        # print(idx, idx_j, answer, saegin, new_str)
        cnt+=1
    return answer