from collections import defaultdict
def solution(id_list, report, k):
    # 1. 누가 누구를 신고했는지에 대한 정보
    # 2. 누가 신고를 얼마나 당했는지에 대한 정보
    
    rep_cnt = [0] * len(id_list)
    name_idx = {name:idx for idx, name in enumerate(id_list)} # 우리는 이름이 주어지면 그 이름이 몇번째 idx인지를 알아야함.
    dt = defaultdict(set)
    for re in report:
        a, b = re.split(" ")
        if b not in dt[a]:
            dt[a].add(b)
            rep_cnt[name_idx[b]]+=1
    answer = [0] * len(id_list)
    for key, a in dt.items():
        for val in a:
            if rep_cnt[name_idx[val]] >= k:
                answer[name_idx[key]]+=1
                
                
    return answer
                



