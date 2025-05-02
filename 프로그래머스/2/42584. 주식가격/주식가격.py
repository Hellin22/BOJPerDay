def solution(prices):
    # 떨어지지 않은 일수를 생각해야함.
    '''
    1 2 3 2 3
    
    1
    1 2
    1 2 3
    stck.top하고 비교했을때 3 -> 2는 떨어짐.
    따라서 3은 (idx하고 같이 저장해야할듯) idx하고 2의 idx 비교해서 1 넣기
    1 2 2
    stck.top은 2이고 새로운건 3 -> 3은 마지막이니까 0 넣고
    1 2 2 3
    0 1 3 4
    
    idx - top.idx
    쭉쭉쭉 진행 -> 결국 stack 사용하면 될거같음.
    '''
    
    stck = []
    answer = [0] * len(prices)
    for i, pri in enumerate(prices):
        while stck and stck[-1][1] > pri:
            # stck에 원소가 있는데 감소한 경우
            idx, price = stck.pop()
            answer[idx] = i - idx
            
                
        stck.append((i, pri)) # 다 뺐으면 추가
    
    for i in range(len(stck)):
        answer[stck[i][0]] = stck[-1][0] - stck[i][0]
    
    return answer