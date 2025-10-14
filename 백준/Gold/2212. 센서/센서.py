import sys
inp = sys.stdin.readline


'''
N개의 센서
K개의 집중국

N개의 센서 좌표 -> 중복값 존재

센서들은 하나의 집중국과는 통신 가능해야함. 집중국 유지비 문제로 집중국의 수신 가능 영역의 길이 합은 최소

각 집중국은 센서의 수신 가능 영역 조절 가능.

집중국도 하나의 좌표를 가짐

모든 센서에 대해서 가장 가까운 집중국 좌표
이 좌표 차이의 합이 최소가 되어야한다.

완탐을 하려면? 백만cK * n -> 시간초과남.

어차피 거리가 1씩 차이나게됨.
따라서 실제로 센서가 많이 있는 곳(겹치게) 집중국을 세우는게 좋음.
만약 센서가 똑같은 개수로 있다면?

k개로 분할하는 방법을 찾기? -> k개 안에 최대한 비슷한 개수로 센서가 존재하면 됨.

센서 개수가 집중국보다 적을수도 있음..

이분탐색?
결국 센서의 위치가 집중국의 위치가 되는건 맞음.
이분탐색으로 하면 2의 배수개가 아닐때 문제 생김. -> 다른 방법 찾기

'''
n = int(inp().strip())
k = int(inp().strip())

llist = list(map(int, inp().strip().split()))
llist.sort()

if k >= n:
    print(0)
    exit()
    
llist2 = []
for i in range(1, n):
    llist2.append(llist[i] - llist[i-1])

llist2.sort()
for i in range(k-1):
    llist2.pop()

print(sum(llist2))