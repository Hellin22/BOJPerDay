'''
1. 연결이 안되어 있을수도 있다. (전체는 항상 연결되어 있음)
2. 어디서부터 시작해야하는가? 선으로 해야해서 2개의 정점이 필요한데

선분에 대해서 진행 -> 가장 COST 적은것만 선택하면 GOOD?
어떻게든 연결이 되어있는지를 확인하면 됨.(1, 3)?
결국 이거 UNION FIND?
-> 연결이 안된 것도 있을 수 있음.
아니지. 무조건 모든게 연결 가능하다고 했음.
FIND(A), FIND(B)가 다르면 연결이 필요한것.

'''

def solution(n, costs):
    answer = 0
    # 굳이 graph를 만들 필요도 없는듯?
    z_cnt = 1
    
    costs.sort(key = lambda x: (x[2]))
    parent = [i for i in range(n)]
    
    def find(a): # a의 부모 노드를 찾는 것.
        if a != parent[a]: 
            parent[a] = find(parent[a])
        return parent[a]
    
    def union(a, b):  # a, b를 합치는 것
        roota, rootb = find(a), find(b)

        if roota == rootb:
            return False  # 이미 같은 집합
        else:
            if roota > rootb:
                parent[roota] = rootb  # roota가 rootb에 붙음
            else:
                parent[rootb] = roota  # rootb가 roota에 붙음
            return True  # 병합 수행됨
    
    for fr, to, cost in costs:
        if find(fr) == find(to): continue
        else:
            answer += cost
            union(fr, to)
    
    return answer