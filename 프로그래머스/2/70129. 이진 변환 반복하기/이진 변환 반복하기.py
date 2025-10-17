def solution(s):
    # 이진 변환 횟수 + 제거된 0의 개수
    # s가 1이 될때까지
    ans = [0, 0]
    while s != "1":
        ori_len = len(s)
        s = s.replace("0", "")
        change_len = len(s)
        ans[0] += 1
        ans[1] += ori_len - change_len
        s = bin(len(s))[2:]        
        
        
    return ans