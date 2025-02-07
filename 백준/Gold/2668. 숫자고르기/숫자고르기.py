import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp())

arr = [0] * (n+1)
for i in range(1, n+1):
    arr[i] = int(inp())

res = set()
'''
7
4
1
1
5
3
4
5
'''
q = deque()
for i in range(1, n+1):
    visit = [[0] * 2 for _ in range(n+1)] # in, out
    llist = []
    q.append(arr[i])
    visit[i][1] = 1 
    visit[arr[i]][0] = 1 
    while q:
        cur = q.popleft()
        if visit[cur][1] == 1: continue
        visit[cur][1] = 1
        visit[arr[cur]][0] = 1
        q.append(arr[cur])

    flag = True
    for i in range(1, n+1):
        if visit[i][0] == 1 and visit[i][1] == 1:
            llist.append(i)
        if visit[i][0] != visit[i][1]:
            flag = False
            break
    if flag: res.update(list(map(int,llist)))

llist = sorted(list(res))
print('\n'.join([str(len(llist))] + list(map(str, [i for i in llist]))))