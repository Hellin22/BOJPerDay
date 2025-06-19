'''
1. 존재하는거 말 or 길이(len)가 1이면 or 이전값의 마지막(prev[-1] != cur[0])이면 탈락

2. 1명 탈락하면 끝나고 가장 먼저 탈락하는 사람 번호(idx+1), 내가 몇번째 말했는지(자신의 몇번째 차례)
-> 총 n명 있음.

만약 탈락자 없으면 [0, 0]
'''


def solution(n, words):
    answer = [0, 0]
    
    if len(words[0]) == 1: # 불가능
        print("AWEeaw")
        
    word_st = set()
    word_st.add(words[0])
    # 이거 굳이 n이 필요한지 모르겠다.
    for i in range(1, len(words)):
        prev, cur = words[i-1], words[i]
        # 1. 이미 말했던거면 안됨.
        if cur in word_st: 
            print(i, i%n+1, i//n+1)
            answer = [i%n+1, i//n+1]
            break
        word_st.add(cur)
        
        # 2. 길이가 1이면 안됨
        if len(cur) == 1:
            print(i, i%n+1, i//n+1)
            answer = [i%n+1, i//n+1]
            break
        
        # 3. prev의 마지막과 cur의 처음은 같아야함
        if prev[-1] != cur[0]:
            print(i, i%n+1, i//n+1)
            answer = [i%n+1, i//n+1]
            break
        
        
        

    return answer