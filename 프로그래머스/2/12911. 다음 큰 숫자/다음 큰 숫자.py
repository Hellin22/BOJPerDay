def solution(n):
    answer = 0
    nxt_n = n
    
    # n보다 큰 자연수
    # n과 1의 개수가 동일함. -> 길이가 다를수도 
    # 길이가 다른 경우만 예외처리 == 길이와 1의 개수가 동일하다? -> 길이 하나 더 길고 처음이 1이고 2번째 비우고 나머지 1
    n = list(bin(n)[2:])
    one_cnt = n.count("1")
    while True:
        nxt_n += 1
        nxt_n_list = list(bin(nxt_n)[2:])
        if nxt_n_list.count("1") == one_cnt:
            return nxt_n
        
    return