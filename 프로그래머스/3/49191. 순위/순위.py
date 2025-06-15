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
'''
def solution(n, results):
    answer = 0

    g1 = [[] for _ in range(n+1)]
    g2 = [[] for _ in range(n+1)]
    
    for a, b in results:
        g1[a].append(b)
        g2[b].append(a)
        
    def dfs(graph, node, visit):
        nonlocal cnt
        for num in graph[node]:
            if visit[num] == 1: continue
            visit[num] = 1
            cnt+=1
            dfs(graph, num, visit)
    
    for i in range(1, n+1):
        cnt = 0
        v1 = [0] * (n+1)
        v2 = [0] * (n+1)
        dfs(g1, i, v1)
        dfs(g2, i, v2)
        if cnt == n-1: answer+=1 
        
    return answer