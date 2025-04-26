'''
직원은 설정 출근희망 + 10분까지 어플로 출근해야함
9시 58분 -> 10시 8분까지 출근해야하
토, 일은 이벤트 영향없음

시각은 
시각 *100 + 분임.
-> //100 -> 시각
% 100 -> 분

'''
def solution(schedules, timelogs, startday):
    answer = 0
    
    # 중요한건 *100 %100이기 때문에 십, 일의자리는 최대 59임
    # 이거만 고려해서 만들어주기
    
    # 희망 출근시간
    for i, sc in enumerate(schedules):
        h, m = int(sc)//100, int(sc) % 100
        m+=10
        if m >= 60:
            m-=60
            h+=1
        schedules[i] = h*100+m
    # startday가 5, 6이면 고려 안한다.
    startday-=1
    for i, time in enumerate(timelogs):
        st = startday
        flag = True # False가 되면 answer에 아무것도 안해줌
        for t in time: # [710, 2359, ...]이 들어있음
            if st % 7 in (5, 6):
                st+=1
                continue
            else:
                if t > schedules[i]:
                    flag = False
                    break
                else: st+=1                
        if flag: answer+=1
    
    return answer