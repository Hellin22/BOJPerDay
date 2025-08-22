def solution(prices):
    
    '''
    주식 가격이 언제 떨어지는지
    뒤에서부터 넣어야할거같음
    
    '''
    
    stck = []
    ans = [0] * len(prices)
    for i in range(len(prices)):
        while stck and stck[-1][0] > prices[i]:
            val, idx = stck.pop()        
            ans[idx] = i-idx

        stck.append([prices[i], i])

    for i, val in enumerate(ans):
        if ans[i] == 0: ans[i] = len(ans)-i-1
    return ans