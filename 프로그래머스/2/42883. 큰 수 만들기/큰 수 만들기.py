'''
stack을 사용해볼까?

4 
4 1
7
stck을 없애는거지 계속

'''

def solution(numbers, k):
    stck = []
    cur_k = 0
    flag = False
    cur_i = 0
    flag = False
    for i in range(len(numbers)):
        if not stck: stck.append(int(numbers[i]))
        else:
            cur = int(numbers[i])
            while stck:
                # 자기보다 작은거 빼야함.
                if stck[-1] >= cur: break
                else: # 현재값이 더 큰 경우(빼아함)
                    stck.pop()
                    cur_k+=1
                    if cur_k == k: 
                        flag = True
                        break
            stck.append(cur)
        if flag: 
            cur_i = i
            break
    
    print(stck, cur_i) # [cur_i:] 하면됨.
    # 만약에 cur_k가 k가 아니라면? 뒤에서 k-cur_k개 빼면됨.
    
    if cur_k == k:
        for i in range(cur_i+1, len(numbers)):
            stck.append(numbers[i])
        sttr = "".join(map(str, stck))
    else:
        for i in range(k-cur_k):
            stck.pop()
        sttr = "".join(map(str, stck))

    return sttr
'''
1. if not stck: numbers[i] 넣기
2. if stck: -> 현재값이 stck[-1]보다 크거나 같으면 넣을 수 있음 
            -> while문을 돌리면서 stck[-1]이 현재값보다 작다 == pop하기 (cur_k+=1)
            -> 만약 stck[-1]이 현재값하고 같거나 크다.(stck[-1] = 9, 현재는 2) == 바로 append
            -> cur_k가 k가 되면 끝. or stck이 비게된다면 끝.

'''