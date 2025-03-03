import sys
from collections import deque
inp = sys.stdin.readline

n, k = map(int, inp().strip().split())
# visit 배열에다가 어디서 왔는지 저장하면 됨
visit = [-1] * 100001
if n == k:
    print(0)
    print(n)
    exit(0)
dq = deque()
dq.append((n, 0)) # 현재값, res
visit[n] = n
llist = []
while dq:
    cur, cnt = dq.popleft()

    for next_pos in (cur+1, cur-1, cur*2):
        if 0<=next_pos<=100000 and visit[next_pos] == -1:
            
            if next_pos == k:
                llist.append(k)
                llist.append(cur)
                tmp_pos = cur
                while tmp_pos != n:
                    llist.append(visit[tmp_pos])
                    tmp_pos = visit[tmp_pos]
                
            dq.append((next_pos, cnt+1))
            visit[next_pos] = cur # visit[nx]에는 부모가 들어감. 

print(len(llist)-1)
print(" ".join(map(str, llist[::-1])))