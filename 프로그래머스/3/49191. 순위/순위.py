'''
n명의 선수 (1~n번의 번호)
1:1로 경기
if a > b: a는 b를 이김

정확하게 순위를 매길 수 있는 선수의 수를 return하기
-> 이거 lg 문제랑 똑같은 느낌이네

선수는 1~100
결과는 4500
-> union find 사용

다른 문제인거같다...
음...
플로이드 와샬?
그래프를 2개 유지? g1은 정방향, g2는 역방향

왜 이걸로 안되는거지?

'''
def solution(n, results):
    answer = 0

    g1 = [[] for _ in range(n+1)]
    g2 = [[] for _ in range(n+1)]
    
    for a, b in results:
        g1[a].append(b)
        g2[b].append(a)
    v1 = [0] * (n+1)
    v2 = [0] * (n+1)
    cnt = 0
    def dfs(node):
        nonlocal cnt
        for num in g1[node]:
            if v1[num] == 1: continue
            v1[num] = 1
            cnt+=1
            dfs(num)
            # v1[num] = 0 # 필요 없을듯
    def dfs2(node):
        nonlocal cnt
        for num in g2[node]:
            if v2[num] == 1: continue
            v2[num] = 1
            cnt+=1
            dfs2(num)
            # v2[num] = 0
    
    for i in range(1, n+1):
        dfs(i)
        dfs2(i)
        if cnt == n-1: answer+=1 
        cnt = 0
        
        v1 = [0] * (n+1)
        v2 = [0] * (n+1)
    
    
    
    return answer