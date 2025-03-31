'''
문자열 다루는게 아직 약한게 느껴지는구만..

'''
def solution(msg):
    answer = []
    dt = dict()
    for i in range(1, 27): # 최초 색인 초기화
        dt[chr(i+64)] = i
    # 1. 현재는 msg[:i] 
    cnt = 0
    while len(msg) != 0:
    # while cnt != 10:
        cnt+=1
        if msg in dt: 
            answer.append(dt[msg])
            break
        
        else:
            for i in range(1, len(msg)+1):
                # print(msg[:i], "hello", i)            
                if msg[:i] not in dt:
                    dt[msg[:i]] = len(dt)+1
                    # print(msg[:i-1], msg[:i])
                    # print(msg)
                    answer.append(dt[msg[:i-1]])
                    msg = msg[i-1:]
                    # print("후",msg)
                    break
            
                    
    return answer