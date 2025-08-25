import math
def solution(fees, records):
    '''
    입차 후 출차기록 없음 -> 23:59
    차량별 누적 주차시간
    1. 주차시간 <= 기본시간 -> 기본요금
    2. 주차시간 > 기본시간 -> 기본요금 + 올림((총 시간-기본시간)/단위시간) * 단위요금
    [180, 5000, 10, 600]
    
    차량번호 작은 자동차부터 순서대로 리턴
    '''
    
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    ans = [] # "차번호, 요금"
    
    car_in_time = dict()
    save_time = dict()
    for record in records:
        ttime, car_num, inout = record.split(" ")
        ttime = int(ttime[:2])*60 + int(ttime[3:])
        if inout == "IN": car_in_time[car_num] = ttime
        else:
            coming_time = car_in_time[car_num]
            save_time[car_num] = save_time.get(car_num, 0) + ttime-coming_time
            del car_in_time[car_num]
                        
    for k, v in car_in_time.items():
        end_time = 23*60+59
        save_time[k] = save_time.get(k, 0) + end_time-v
    
    for k, v in save_time.items():
        if v <= basic_time:
            ans.append((k, basic_fee))
        else:
            ans.append((k, basic_fee + int(math.ceil((v-basic_time)/unit_time)*unit_fee)))
    
    ans.sort(key = lambda x : x[0])
    return [j for i, j in ans]
    