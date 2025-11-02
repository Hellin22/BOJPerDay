import sys
inp = sys.stdin.readline

'''
n개의 통에 초콜릿
1. 초콜릿 개수 오름차순 정렬 
1번째 통의 초콜릿 개수 <= 2번째 <= ...

K<i인 i를 골라 i-K번째 통에 있는 초콜릿 개수와 같아질 때까지 i번째 통에서 초콜릿 꺼내기
통을 재정렬 -> 오름차순으로 배치

n, k
초기 초콜릿 개수

1 2 2 3

k보다 큰 i를 고름.
2보다 큰 i를 고름.

-> 항상 제일 뒤에꺼를 고르면 안되나?
-> 항상 제일 큰거를 고르는게 좋은 방법은 아닌듯
왜냐하면 i-k번째 통의 초콜릿과 같은 개수로 맞춰야 하기 때문.
k+1번째를 항상 처리하면서
k+1이 같다면 k+2, k+3 ...으로 처리

n은 2000 -> n


'''

n, k = map(int, inp().strip().split())

answer, answer_time = 0, 0 # 초콜릿 최대 개수, 최소 날짜

llist = list(map(int, inp().strip().split()))
llist.insert(0, 0)

while True:
    cur_k = k+1
    # i(cur_k)를 골라서 i-k와 같은지 확인
    while cur_k <= n and llist[cur_k - k] == llist[cur_k]: # cur_k == i
        cur_k+=1
    if cur_k > n: # 더이상 진행 x
        break

    answer += llist[cur_k] - llist[cur_k-k]
    answer_time+=1
    llist[cur_k] = llist[cur_k-k]
    llist.sort()
    
print(answer, answer_time)