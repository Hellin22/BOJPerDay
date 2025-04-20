'''
1. 각 집합은 자연수 n개로 구성

최고의 집합이란?
1) 각 원소의 합이 S가 되는 수의 집합
2) 위 조건을 만족하면서 각 원소의 곱이 최대가 되는 집합

ex) 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합
{ 1, 8 }, { 2, 7 }, { 3, 6 }, { 4, 5 }

그 중 곱셈의 결과가 가장 큰 4*5가 (자연수 2개 + 합이 9)인 집합중 최고의 집합

n(몇개의 원소)
s(합)
이중 최고의 집합(곱이 제일 리스트)를 구해라.

'''
def solution(n, s):
    answer = []
    
    # 1. n은 1~10000 -> 완전탐색(백트래킹)으로는 불가능
    # 2. s는 십만 -> 곱이 커야하니까 절바능로 계속 나누기?
    # 3. 불가능하면 [-1] -> n < s == -1  -> n==s라면 [1, 1, ..., 1]
    if s < n: return [-1]
    if n == s: return [1 for i in range(n)]
    else:
        cnt = s % n # 이 개수만큼 -1한 값을 추가해야함
        num = s // n
        
        cur_cnt = 0
        if cnt == 0: # 딱 나눠떨어지는 경우
            answer.extend([num] * n)
        else:
            for i in range(n):
                if cur_cnt != cnt:
                    answer.append(num+1)
                    cur_cnt+=1
                else: answer.append(num)
        answer.sort()
    
    
    return answer