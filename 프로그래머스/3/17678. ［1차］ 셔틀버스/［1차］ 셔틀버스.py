'''
콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각
-> 콘은 같은 시간에 도착한 크루 중 가장 뒤에 선다.

셔틀은 9시부터 n회 t분 간격으로 도착, 최대 m명 탑승

'''
from collections import deque
def solution(n, t, m, timetable):
    for i, time in enumerate(timetable):
        timetable[i] = int(time[:2]) * 60 + int(time[3:]) 
    timetable.sort()
    timetable = deque(timetable)
    
    cur_time = 540 # 9시 버스 출발시간
    min_time = 0 # 사람이 탈 수 있는 최소 시간
    final_flag = False
    for bus_cnt in range(n):  # n이 버스의 개수 -> 1. 버스 개수만큼 for문 돌리기 
        # 2. bus 한대당 m명의 사람을 태울 수 있음.
        # timetable을 보면서 가능한 사람을 모두 태우기(최대 m명)
        cur_m = 0 # 현재 탑승한 사람 수
        
        while timetable and timetable[0] <= cur_time: # 버스에 탑승 가능하다면
            min_time = timetable.popleft() # 최소 시간
            cur_m+=1
            if cur_m == m: break # 다 찼으면 종료
        # 3. t 시간이 지날때마다 bus가 새로 옴. -> cur_time += t
        if bus_cnt == n-1 and cur_m == m: # 마지막 버슨데 cur_m이 m
            # 이 말은 min_time-1을 해줘야 한다는 의미
            final_flag = True
            
        cur_time += t
    
    # 만약 아무도 못타는 사람이 있다는 가정 or 저 뒤에 있는 못타는 사람 있다는 가정
    # 그러면 다르게 접근해야함.
    # 9시부터 t시간 뒤의 시간 (540 + t*n) -> 버스가 마지막으로 오는 시간
    final_time = 540 + t*(n-1) # 마지막으로 버스 도착하는 시간 
    if final_flag == True: # min_time-1 해주기
        min_time -= 1
    else:
        min_time = max(final_time, min_time)
    
    # print(final_time, min_time)
    # min_time = max(final_time, min_time-1) # 여기서 중요한거는 min_time-1이 아닐수도 있다는 것. min_time이어도 가능(max로 하기?)
    return f"{min_time//60:02d}:{min_time%60:02d}"
