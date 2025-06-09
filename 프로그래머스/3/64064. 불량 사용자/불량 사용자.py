'''
user_id, banned_id는 모두 1~8개
각 원소는 최대 8자리

경우의 수를 찾는 문제

dfs로 백트래킹 적용? -> 8개 밖에 없기 때문
순서가 다른건 똑같은것. 하지만 매칭되는 순서가 다른거도 똑같은것.
순열은 순열인디... -> 전체 map을 하나씩 가지고 있어야하는가? -> 어떠한 배열을 sort해서 set에다가 저장해놓으면 되지 않을까? == 중요한건 sort를 해야한다는 것
'''
def solution(user_id, banned_id):
    answer = 0
    all_set = set() # 경우의 수를 tuple로 저장하여 중복을 없애는 set
    
    cur_list = [] # dfs에 대해서 현재 값(배열)을 저장하고 있을 리스트
    n = len(user_id) # user_id의 수
    m = len(banned_id) # cur_list의 크기 제한 -> len(cur_list) == m이 되면 all_set에 추가
    visit = [0] * n
    def dfs(n, m, cur_ban_idx):
        if len(cur_list) == m: # cur_list의 크기가 m이 되면 종료
            sort_list = sorted(cur_list)            
            cur_tuple = tuple(sort_list)
            all_set.add(cur_tuple)
            return
        
        for i in range(n):
            if visit[i] == 1: continue
            if len(user_id[i]) != len(banned_id[cur_ban_idx]): continue # ban의 길이와 id 길이 다르면 continue
            
            # 여기까지 온거면 길이 같은것 -> "*" 제외하고 같은지 확인하기
            flag = True
            for j in range(len(banned_id[cur_ban_idx])):
                if banned_id[cur_ban_idx][j] == "*": continue
                if banned_id[cur_ban_idx][j] != user_id[i][j]: 
                    flag = False
                    break
            if not flag: continue

            # 모든 조건에 다 성립
            visit[i] = 1
            cur_list.append(user_id[i])
            dfs(n, m, cur_ban_idx+1)
            cur_list.pop()
            visit[i] = 0
    
    dfs(n, m, 0)
    
    answer = len(all_set)
    
    return answer