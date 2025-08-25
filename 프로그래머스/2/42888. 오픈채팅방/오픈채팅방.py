def solution(record):
    '''
    Enter 아이디 닉네임 -> 닉네임님이 들어왔습니다.
    Leave 아이디 -> 닉네임님이 나갔습니다.
    Change 아이디 닉네임 -> 
    공백 구분
    잘못된거 x
    
    아이디 - 닉네임
    ans에는 1 2(들어오고 / 나가고), 아이디
    이렇게만 구성해놓으면 될듯
    '''
    id_dt = dict()
    ans = []
    for rc in record:
        if rc[0] == "E":
            cmd, id, nickname = rc.split(" ")
            ans.append((1, id))
            id_dt[id] = nickname    
        elif rc[0] == "L":
            cmd, id = rc.split(" ")
            ans.append((2, id))
        else:
            cmd, id, nickname = rc.split(" ")
            id_dt[id] = nickname
            
    for i in range(len(ans)):
        if ans[i][0] == 1:
            ans[i] = f"{id_dt[ans[i][1]]}님이 들어왔습니다."
        else:
            ans[i] = f"{id_dt[ans[i][1]]}님이 나갔습니다."
            
    return ans