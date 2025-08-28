def solution(times):
    
    '''
    최대 1000개니까 완탐 가능할듯
    10분간 사용 불가능
    
    1. 모두 분으로 바꾸기
    
    times를 돌면서 시작하기 전에
    배열을 돌면서 뺄 수 있는 곳은 빼주기
    
    그다음 아무데나 넣기
    if 아무데나 못넣는다 -> append해서 크기 늘려주기
    
    10분간 청소해야하니까 끝 시간에 +10 하기
    
    '''
    times.sort(key = lambda x: x[0])
    
    def cht_minute(sttr):
        return int(sttr[:2]) * 60 + int(sttr[3:])
    
    
    # 1.분으로 변환
    for i in range(len(times)):
        fir, sec = times[i]
        times[i] = [cht_minute(fir), cht_minute(sec)+10]
    
    rooms = []
    # 2. times를 돌면서 진행
    for fir, sec in times:
        if rooms:
            cnt = 0
            for j in range(len(rooms)):
                # rooms에서 빠지는게 있으면 빼기
                if not rooms[j] or rooms[j][1] <= fir:
                    rooms[j] = []
                    cnt+=1
            if cnt == 0:
                rooms.append([fir, sec])
            else:
                for j in range(len(rooms)):
                    if rooms[j] == []:
                        rooms[j] = [fir, sec]
                        break
        else:
            rooms.append([fir, sec])
    return len(rooms)    