from collections import Counter

def solution(X, Y):
    answer = ''
    
    '''
    X, Y에 공통적으로 나오는 숫자를 카운트해주기
    숫자는 0~9이므로 dict로 유지하기
    '''
    dt = dict()
    for i in X:
        dt[i] = dt.get(i, 0) + 1
    
    
    llist2 = [0] * 10
    flag = False   
    ls = []
    for i in Y:
        if i in dt and dt[i] != 0:
            flag = True
            # ls.append(int(i))
            llist2[int(i)]+=1
            dt[i]-=1
    # ls.sort(key = lambda x: -x)
    z_flag = False
    if not flag: return "-1"
    else:
        for i in range(9, -1, -1):
            if i != 0 and llist2[i] != 0:
                z_flag = True
            ls.extend(str(i) * llist2[i])
    
    if z_flag == False: return "0"
    
    answer = "".join(map(str, ls))
    return answer