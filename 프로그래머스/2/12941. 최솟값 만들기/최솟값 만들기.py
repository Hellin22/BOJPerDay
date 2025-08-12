'''
a*b의 합이 최소가 되도록하기
작은거, 큰거 곱하기 
'''
def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    return sum(a*b for a, b in zip(A, B))