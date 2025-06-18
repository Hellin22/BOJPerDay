'''
항상 ICN에서 출발
방문하는 공항 경로를 배열에 담아서 리턴
공항 개수는 10,000개
tickets는 [a, b] a->b 의미
항공권은 "무조건" 다 써야함
경로 2개이상 -> 순서 앞서는거 먼저 사용

사용한 경로는 pop하면 됨. 미리 다 정렬 해놓으면?

아.... 가능하지 않은 경로는 가면 안되는구나...
즉 무조건 알파벳순으로 작은곳을 가는게 아니라 갈 수 있다면. 즉, 다시 리턴할 수 있다면 간다...
이게 무슨말이지?
그러면 무조건 완탐을 해야하는건데 ㅋㅋㅋ 후
'''
from collections import defaultdict
def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    
    for a, b in tickets:
        graph[a].append([b,0])
    
    # graph의 모든 노드 돌면서(keys) 역알파벳순 정렬 -> pop. graph[k].sort(역방향)
    for k in graph.keys():
        graph[k].sort() # 앞에서부터 오름차순
    
    all_cnt = len(tickets)
    cur_cnt = 0
    
    def dfs(node):
        nonlocal cur_cnt, all_cnt
        
        
        if all_cnt == cur_cnt:
            return True
        
        for i in range(len(graph[node])):
            name, visited = graph[node][i][0], graph[node][i][1]
            # if graph[node][i][1] == 0: # 경로 존재한다면
            if visited == 0: # 경로 존재한다면
                graph[node][i][1] = 1
                cur_cnt+=1
                answer.append(name) # answer에 추가하기
                
                flag = dfs(name)
                
                if not flag: # 불가능
                    graph[node][i][1] = 0
                    cur_cnt-=1
                    answer.pop() # answer에서 빼기(제일 뒤)
        # print("현재값들", node, all_cnt, cur_cnt)
        if all_cnt != cur_cnt: # 가능한 모든 경우 다 봤는데 안됨 == 불가능한 경로
            return False
        
        return True # 가능
    
    # ICN에서부터 출발
    answer.append("ICN")
    dfs("ICN")
    return answer