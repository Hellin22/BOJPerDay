'''
a*b의 합이 최소가 되도록하기
작은거, 큰거 곱하기 
'''
def solution(A,B):
    A.sort()
    B.sort(key = lambda x: -x)
    ans = 0
    for i in range(len(A)):
        ans += A[i]*B[i]
    return ans