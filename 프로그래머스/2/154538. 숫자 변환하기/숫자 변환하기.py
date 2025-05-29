'''
bfs 진행 -> x+n, 2x, 3x -> 항상 기존값보다 커짐 -> 만약 y보다 커지면 해당숫자는 추가x

'''

from collections import deque

def solution(x, y, n):
    answer = 0
    
    llist = [0] * 1000001
    if x == y: return 0
    dq = deque()
    dq.append((x, 0))
    while True:
        if not dq: return -1
        
        pl, cnt = dq.popleft()
        fir, sec, thr = pl+n, pl*2, pl*3
        if fir == y: return cnt+1
        if sec == y: return cnt+1
        if thr == y: return cnt+1
        
        if fir < y and llist[fir] == 0: 
            dq.append((fir, cnt+1))
            llist[fir] = 1
        if sec < y and llist[sec] == 0: 
            dq.append((sec, cnt+1))
            llist[sec] = 1
        if thr < y and llist[thr] == 0:
            dq.append((thr, cnt+1))
            llist[thr] = 1
        
        
    return -1