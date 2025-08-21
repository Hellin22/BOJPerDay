
def solution(numbers):
    
    '''
    자신보다 크면서 가장 가까이에 있는 수 찾기 -> 없으면 -1
    뒤에서 하기 or 첨부터 하기?
    9 1 5 3 6 2 
    
    '''
    res = [-1] * len(numbers)
    stck = []
    for i, val in enumerate(numbers):
        if not stck or stck[-1][1] >= val:
            stck.append([i, val])
        else:
            while stck and stck[-1][1] < val:
                tmp_i, tmp_val = stck.pop()
                res[tmp_i] = val
            stck.append([i, val])
            
    return res