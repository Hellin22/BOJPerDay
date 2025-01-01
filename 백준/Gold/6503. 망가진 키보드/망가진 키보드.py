import sys

inp = sys.stdin.readline

# 입력이 0이 나오면 종료
while True:
    m = int(inp().strip())
    if m == 0: exit()
    line = inp().strip()

    # two pointer 사용하기
    # dictionary 사용하고 key는 문자, value는 개수 저장하기
    # maxx (dict key 개수 갱신), 만약 right을 옮겼을때 key가 m보다 많아짐
    # 그렇게되면 key가 m과 같아질때까지 left를 한칸씩 옮김 -> left, right idx 위치 필요
    # 최종적으로 print(res) 출력해주기
    ddict = dict()
    maxx, left = -1, 0
    for right in range(len(line)):
        # in 함수 사용
        if line[right] not in ddict:
            # 만약 맵 안에 있다면 개수 추가하기. 없다면 새롭게 추가하기(1로)
            ddict[line[right]] = 1
        else:
            ddict[line[right]] += 1
        
        # 만약 key의 개수가 m을 넘어선다면 left 이동
        while(len(ddict) > m):
            ddict[line[left]]-=1
            if(ddict[line[left]] == 0):
                ddict.pop(line[left])
            
            left+=1
        
        maxx = max(maxx, right - left + 1)
    print(maxx)
