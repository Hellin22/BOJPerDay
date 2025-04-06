'''
음악 제목, 재생이 시작되고 끝난 시각, 악보

음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개

음악은 항상 처음부터 
-> 만약 음악 길이가 더 길다
-> 음악이 끊김없이 처음부터 반복재생
-> 더 짧다? (음악이 다 재생 못하는것)
-> 처음부터 재생시간 만큼만

조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
'''

'''
musicinfos의 시간만큼 저걸 바꿔야하지 않을까 싶다.

fir, sec, title, music = musicinfos[i].strip().split(",")
1. fir = int(fir[:2]) * 60 + int(fir[3:])
    sec = fir과 동일하게 진행
2. sec-fir을 해서 music를 줄여야할지 늘려야할지 정해야함.

중요한 문자열 비교를 어떻게 할것인가...
완탐..?
그래서 조건이 일치한다 -> 재생시간 제일 긴거, idx
즉, -(sec-fir), idx로 정렬하기
비어있으면 return
아니라면 return musicinfos[list[0][1]][2]

"ABCDEFG"
["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
'''


def solution(m, musicinfos):
    answer = ''
    # c#은 하나의 음임
    # 이걸 먼저 진행해야할듯? 
    
    dt = {
        "C#": "1", "D#": "2", "F#": "3", "G#": "4", "A#": "5"
    }
    
    for sharp, rep in dt.items():
        m = m.replace(sharp, rep)
    
    for i in range(len(musicinfos)):
        fir, sec, title, music = musicinfos[i].strip().split(",")
        print(fir, sec, title, music)
        fir = int(fir[:2]) * 60 + int(fir[3:])
        sec = int(sec[:2]) * 60 + int(sec[3:])
        
        for sharp, rep in dt.items():
            music = music.replace(sharp, rep)
        print(music)
    
        # sec-fir보다 짧을 경우를 고려 안해줌.
        if len(music) > sec-fir:
            music = music[:sec-fir]
        else:
            tmp_music = music
            music_size = len(music)
            for j in range((sec-fir)//music_size):
                music += tmp_music
        
            music += tmp_music[:sec-fir-len(music)]
        
        musicinfos[i] = (fir, sec, title, music)
    
    llist = []
    for i in range(len(musicinfos)):
        if m in musicinfos[i][3]:
            llist.append((-(musicinfos[i][1] - musicinfos[i][0]), musicinfos[i][0], i))
            # 먼저 입력되었다는게 fir이 작은걸 읨미?
    
    if not llist:
        return "(None)"
    
    llist.sort()
    return musicinfos[llist[0][2]][2]
