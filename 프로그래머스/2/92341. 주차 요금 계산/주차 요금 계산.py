import math
'''
주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 
차량별로 주차 요금을 계산
잘못된 입력은 주어지지 않습니다

모든 차량의 입차 출차 기록 계산
1. 입차는 무조건 존재
2. 출차는 없을수도 있음. -> 없으면 23:59로 책정

fees [180, 5000, 10, 600] 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
records ["05:34 5961 IN","06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

일단 records는 1개가 3개로 구성됨.
즉, records[i]는 3개의 구성요소 split(" ") 하면될듯?
records에 대해서 돌면서 저걸 진행?

일단 IN이다? -> key(차량번호) <-> val(시간(분으로 환산))
OUT이다? -> key에 대한 val 가져옴. 현재 시간(분) - val을 해서 -fees[0] 진행.
만약 a-fees[0]가 <= 0이면 그대로
차량번호 작은 순서대로 answer에 넣어야함.
즉, 차량번호를 알고있어야하는것. -> 4자리 str이니까 그냥 moneys = dict()
moneys[차량번호] = moneys.get(차량번호, 0) + 요금
-> dt에서 바로 계산때리지 말고
ttime = dict()로 진행하기

dt는 입출차 계산 dict
ttime은 누적시간 계산 dict
moneys는 돈계산 dict

누적주차시간을 체크해야함.

주차요금은?


fees [180, 5000, 10, 600] 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
records ["05:34 5961 IN","06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

'''

def solution(fees, records):
    answer = []
    # 23:59분 계산(분)
    maximum = 23*60 + 59
    
    dt = dict()
    ttime = dict()
    moneys = []
    for i, record in enumerate(records):
        llist = list(record.split(" "))
        print(llist)
        if llist[2] == "IN":
            dt[llist[1]] = int(llist[0][0]) * 600 + int(llist[0][1]) * 60 + int(llist[0][3]) * 10 + int(llist[0][4])
            print(dt[llist[1]])
        elif llist[2] == "OUT":
            # OUT인 경우에는 dt에 있는 값을 빼면됨.
            a = int(llist[0][0]) * 600 + int(llist[0][1]) * 60 + int(llist[0][3]) * 10 + int(llist[0][4])
            ttime[llist[1]] = ttime.get(llist[1], 0) + a-dt[llist[1]]
            del dt[llist[1]]
            
    print(dt, ttime)
    
    # dt에 남아있는거 == 23:59분 출차
    for key, val in dt.items():
        ttime[key] = ttime.get(key, 0)+ (maximum-val)

    # ttime에는 ("차량 번호", "누적 시간")
    for key, val in ttime.items():
        if val < fees[0]: # 기본시간보다 이하면 그대로
            moneys.append((key, fees[1]))
        else:
            moneys.append((key, fees[1] + math.ceil((val-fees[0])/fees[2]) * fees[3]))
    
    print(moneys)
    moneys.sort()
    return [y for x, y in moneys]
    
    return ", ".join(str(y) for x, y in moneys)