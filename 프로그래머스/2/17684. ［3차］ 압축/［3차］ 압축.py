
def solution(msg):
    
    
    '''
    LZW로 압축 -> 복호화를 해야함
    길이가 1인 모든 단어 포함 사전 초기화
    2.사전에서 현재 입력과 일치하는 가장 긴 문자열 w
    w에 해당하는 사전의 색인 번호 출력, 입력에서 w 제거(메시지에서 w 제거)
    처리되지 않은 다음 글자 c -> w+c를 사전에 등록
    2로 돌아감
    
    msg를 모두 봄
    if 등록 ㅇ -> 등록된거 번호 출력 후 계속 이어나감
    elif 등록 x -> 색인번호 추가로 등록(len +1)
    
    등록 안된게 처음 나온다. -> 그러면 다음껄로 넘어가는듯?
    w는 1개로 무조건 출발함 -> 하나씩 무조건 보면됨
    '''
    # "A":1
    dt = {chr(i+65):i+1 for i in range(26)}
    ans = []
    # msg의 문자 하나씩 보기
    i = 0
    cnt = 0
    # while cnt != 10:
    while i != len(msg):        
        for j in range(i+1, len(msg)+1):
            w = msg[i:j]
            if w not in dt: # 만약에 이 숫자가 없다면 -> 그 이전 값을 ans에 추가
                ans.append(dt[w[:-1]])
                dt[w] = len(dt)+1
                i = j-1
                break
            elif w in dt and j == len(msg):
                ans.append(dt[w])
                i=len(msg)
                break
        cnt+=1
    return ans