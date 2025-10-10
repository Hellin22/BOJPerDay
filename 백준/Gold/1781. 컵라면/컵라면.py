from heapq import heappush, heappop
import sys
inp = sys.stdin.readline


'''
동호에게 n개의 문제 -> 문제를 풀었을때 컵라면 몇개 줄건지 제시
각 문제는 데드라인이 존재

데드라인과 컵라면 수가 있음.
동호가 받을 수 있는 최대 컵라면 수를 구해야함.

n은 20만
(데드라인과 컵라면 수) -> 문제 푸는데에는 단위시간이 걸림
(a, b)

a 작은순, b 큰순으로 정렬

a가 같은거 모두 pop


'''

n = int(inp().strip())
llist = []
hq = []
for _ in range(n):
    a, b = map(int, inp().strip().split())
    llist.append((a, b))
llist.sort(key = lambda x:(x[0], x[1])) # 데드라인, 라면

for dl, ramen in llist:
    heappush(hq, ramen)
    if len(hq) > dl:
        heappop(hq)
print(sum(hq))
