'''
data = 
[[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
'''

def solution(data, ext, val_ext, sort_by):

    dt = {"code": 0, "date":1, "maximum":2, "remain":3}
    answer = []
    for i in data:
        if i[dt[ext]]< val_ext:
            answer.append(i)
    answer.sort(key = lambda x: x[dt[sort_by]])
    
    
    return answer