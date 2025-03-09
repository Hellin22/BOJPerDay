import sys
import math
inp = sys.stdin.readline

'''
첫 번째 줄에 굴다리의 길이 N 이 주어진다. (1 ≤ N ≤ 100,000)

두 번째 줄에 가로등의 개수 M 이 주어진다. (1 ≤ M ≤ N)

다음 줄에 M 개의 설치할 수 있는 가로등의 위치 x 가 주어진다. (0 ≤ x ≤ N)

가로등의 위치 x는 오름차순으로 입력받으며 가로등의 위치는 중복되지 않으며, 정수이다.
5
2
2 4

출력:
굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이를 출력한다.
2
'''
'''
le가 있고 ri가 있을때, 
'''

n = int(inp().strip())
m = int(inp().strip())
switch_idx = list(map(int, inp().strip().split()))

cur = switch_idx[0]
res = switch_idx[0]

for i in range(len(switch_idx)-1):
    res = max(res, math.ceil((switch_idx[i+1] - switch_idx[i])/2))
    cur = switch_idx[i+1]

res = max(res, n-switch_idx[-1])

print(res)
