'''
1. 모든 사원이 무작위 자연수 하나씩
2. 사원은 한번씩 경기
3. 경기당 A팀 1명, B팀 1명 나와서 서로의 수를 공개 -> 숫자가 큰쪽이 승리
    -> 승리한팀 +1 a_score, b_score
    -> 비기면 아무도 점수 안얻음

4. a팀은 이미 출전순서 o
-> 이걸 보고 b팀이 얻을 수 있는 최대 점수는?

그리디 사용?
큰 점수에는 큰사람이 하기만 하면 되지않나?
-> 이걸 어떻게 찾을것인가

a팀의 최고점 -> b팀의 최고점
이렇게 하나씩 빼면서 하면 되지 않나?
근데 버리는패로 가야할수도 있음
-> a의 최고점 -> b의 최소점 -> 버리기

if a.max >= b.max -> a는 pop. but, b는 pop 안함
'''
import heapq
def solution(A, B):
    # a, b의 크기는 십만까지 가능 -> n^2 안됨
    answer = -1
    A = [-i for i in A]
    B = [-i for i in B]
    heapq.heapify(A)
    heapq.heapify(B)
    b_score = 0
    while A: # A에서는 무조건 하나씩 빼기 때문
        if -A[0] < -B[0]: # B가 더 큰경우
            heapq.heappop(B)
            b_score+=1
        heapq.heappop(A)
            
    return b_score