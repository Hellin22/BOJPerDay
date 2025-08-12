'''
n의 다음 큰숫자 구하기

n보다 커야함
n을 2진수로 변환했을 때 1 개수 같음
위를 만족하는 가장 작은 수

n은 백만
완탐을 한다면?
2진수 찾는거는 log시간, 1 count 시간

그렇게 안큼
'''

def solution(n):
    cnt = bin(n)[2:].count('1')
    
    while True:
        n+=1
        if cnt == bin(n)[2:].count('1'):
            return n
    