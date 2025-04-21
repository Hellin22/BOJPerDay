'''
string 자체를 저장?
그리고 저장된다 -> set에 없었다 == 
id_list는 최대 1000임

report는 최대 200,000
report에는 "a b" 형태로 띄어쓰기로 구분

k는 200 -> 문제는 이미 신고가 다 된 사람을 처리해줘야 하는가?

set_list를 만들기.
set_list[0]는 id_list[0]를 의미 -> dt로 전부 처리해주기
ex) dt[id_list[idx]] = idx
이런식으로
report_cnt = [0] * len(report)
report[dt[id_list[b]]] += 1 # 이렇게 처리하기 (신고 당한것)

dt_list에 "사람 이름" : idx로 추가하기

for re in report:
    a, b = re.split(" ") # a가 b를 신고한것.
    report[dt[id_list[b]]]+=1 # b가 신고당해서 신고카운트 1 증가
    set_list[dt[id_list[a]]].add(dt_list[b]) # a가 b를 신고(idx로 처리)
'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dt = dict()
    st_list = [set() for _ in range(len(id_list))]
    for i, name in enumerate(id_list):
        dt[name] = i
    reported_cnt = [0] * len(id_list)
    for re in report:
        a, b = re.split(" ")
        # a b는 모두 "muzi", "froodo"처럼 string임
        leen = len(st_list[dt[a]])
        st_list[dt[a]].add(dt[b]) # a가 b를 신고했다는거 추가
        if leen == len(st_list[dt[a]]): # 만약 길이가 같다면 추가가 안된것 == 중복처리한것
            continue # 중복처리면 신고카운트 증가 안시킴
            
        reported_cnt[dt[b]] += 1 # 해당 사람 신고+1
        
        
    # 1000명 -> 1000번 진행 -> 가능할거같음. o(1)에 찾으니까
    for idx, cnt in enumerate(reported_cnt):
        if cnt >= k: # 만약 신고를 k번 이상 당했다면
            for i, sttr in enumerate(id_list): # id_list의 사람들의 result값 증가시킬지 말지 선택
                if idx in st_list[i]: # 만약에 이사람이 신고한 적이 있다면
                    answer[i]+=1
    
    
    
    return answer




