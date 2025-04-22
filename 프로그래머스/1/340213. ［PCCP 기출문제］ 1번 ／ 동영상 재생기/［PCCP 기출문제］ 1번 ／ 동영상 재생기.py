'''
video_len = 영상의 총 길이
pos = 기능이 수행되기 직전의 재생 위치 -> 해당 위치에서 붙터 command가 수행된다는 의미
op_start = 오프닝 시작 시간
op_end = 오프닝 끝나는 시간
commands = 사용자의 입력

for commands -> 최종 영상의 위치를 "mm:ss"로 리턴

commands -> prev, next, 건너뛰기
건너뛰기는 어떠한 command를 수행하기 전 op_st, op_end 사이라면 op_end로 바꾼 후 적용
어떠한 command를 수행한 후에 op_st, op_end 사이라면 op_end로 바꾼 후 적용

'''

def ch_to_sec(sttr):
    return int(sttr[:2]) * 60 + int(sttr[3:])
def ch_to_min(intt):
    minute, sec = divmod(intt, 60)
    return f"{minute:02d}:{sec:02d}"
    
    
def solution(video_len, pos, op_st, op_end, commands):
    answer = ''
    # 모든걸 초로 만들기
    video_len = ch_to_sec(video_len)
    pos = ch_to_sec(pos)
    op_st = ch_to_sec(op_st)
    op_end = ch_to_sec(op_end)
    
    for cmd in commands:
        # 먼저 명령 수행 전에 pos가 op_st, op_end 사이인지 확인
        if op_st <= pos < op_end:
            pos = op_end
        
        if cmd == "next":
            pos = min(pos+10, video_len)
        else:
            pos = max(0, pos-10)
        if op_st <= pos < op_end:
            pos = op_end
            
    return ch_to_min(pos)
    