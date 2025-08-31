def solution(m, musicinfos):
    '''
     C, C#, D, D#, E, F, F#, G, G#, A, A#, B
     음악시간이 길면 반복재생
     음악시간이 짧으면 처음부터 그까지
     
     여러개 -> 재생 시간이 제일 긴것
     
     없으면 (None)
    
    m은 네오의 멜로디 문자열
    음악 시작 시간 / 끝난 시간 / 음악 제목 / 악보 정보
    재생된 시간 제일 긴 것
    -> 
    '''
    def ch_to_minute(ttime):
        return int(ttime[:2]) * 60 + int(ttime[3:])
    
    infos = [] # [시간 차이, 제목, 그만큼의 곡]
    
    def ch_shop(sttr):
        sttr = sttr.replace("C#", "Z")
        sttr = sttr.replace("D#", "W")
        sttr = sttr.replace("F#", "Q")
        sttr = sttr.replace("G#", "P")
        sttr = sttr.replace("A#", "O")
        sttr = sttr.replace("E#", "R")
        sttr = sttr.replace("B#", "T")
        
        return sttr
        
    # c# d# f# g# a# -> 다른걸로 바꾸기
    # C D E F G A B
    # C# -> Z / D# -> W / # F# -> Q / G# -> P / A# -> O
    m = ch_shop(m)
    for music in musicinfos:
        prev, aft, name, gog = music.split(",")
        time_minus = ch_to_minute(aft) - ch_to_minute(prev)
        if time_minus <= 0: continue
        gog = ch_shop(gog)
        gog = (gog * (time_minus // len(gog) +1))[:time_minus]
        
        if gog.find(m) != -1:
            infos.append([time_minus, name, gog])
        
    infos.sort(key = lambda x: -x[0])
    return infos[0][1] if len(infos) != 0 else "(None)"
    