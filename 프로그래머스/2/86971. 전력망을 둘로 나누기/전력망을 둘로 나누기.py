from collections import deque
def solution(n, wires):
    answer = -1
    
    '''
    송전탑 선 하나를 없앨거임
    
    bfs 할꺼임
    set으로 진행하면 어떨까?
    배열로 하면 find해서 삭제하는데 o(n)이니까 set에 저장?
    그러면 노드 배열 안에 set 저장?
    '''
    minn = 100000
    
    graph = [set() for _ in range(n+1)]
    for wa, wb in wires:
        graph[wa].add(wb)
        graph[wb].add(wa)
    
    dq = deque()
    
    for i in range(len(wires)):
        wa, wb = wires[i][0], wires[i][1]
        # 현재꺼 빼기
        graph[wa].discard(wb)
        graph[wb].discard(wa)
        
        if i != 0:
            # 이전꺼는 추가
            pwa, pwb = wires[i-1][0], wires[i-1][1]
            graph[pwa].add(pwb)
            graph[pwb].add(pwa)
    
        # bfs 시작
        dq = deque()
        visit = [0] * (n+1)
        cnt = 1
        dq.append(1)
        visit[1] = 1
        while dq:
            node = dq.popleft()
            for k in graph[node]:
                if visit[k] == 0:
                    dq.append(k)
                    visit[k] = 1
                    cnt+=1
        print(n, cnt)
        minn = min(minn, abs(n-cnt-cnt))
    return minn