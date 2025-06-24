'''
윈도우 슬라이싱
10일간 -> left는 0, right도 처음에 0 -> right 하나씩 늘려가면서 9까지
정확히 일치하면 끝낸다고함.
'''
def solution(want, number, discount):
    left, right = 0, 9
    res = 0
    dt = dict()#
    for i, pwant in enumerate(want):
        dt[pwant] = number[i]
    
    for i in range(10):
        if discount[i] in dt:
            dt[discount[i]]-=1
    flag = True
    for val in dt.values():
        if val != 0:
            flag = False
            break
    if flag:
        res+=1
    
    while right != len(discount)-1:
        if discount[left] in dt:
            dt[discount[left]]+=1
        left+=1
        right+=1
        if discount[right] in dt:   
            dt[discount[right]]-=1  
        
        flag = True
        for val in dt.values():
            if val != 0:
                flag = False
                break
        if flag:
            res+=1
            
    return res
