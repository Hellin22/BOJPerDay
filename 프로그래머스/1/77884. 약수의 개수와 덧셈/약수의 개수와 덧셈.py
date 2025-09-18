def solution(left, right):
    '''
    LEFT ~ RIGHT
    약수 개수가 짝수인 수는 더하고
    홀수인 수는 빼기    
    '''
    
    dp = [2] * (right+1)
    dp[1] = 1
    
    for i in range(left, right+1):
        for j in range(2, i-1):
            if i % j == 0: dp[i]+=1

    # left ~ right까지의 합 or 차
    answer = 0
    for i in range(left, right+1):
        if dp[i] % 2 == 0:
            answer = answer+i
        else: answer -= i
    return answer