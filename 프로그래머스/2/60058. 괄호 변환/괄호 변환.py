def reverse_gwalho(sttr):
    r_str = ""
    for ch in sttr:
        if ch == "(":
            r_str+=")"
        else: r_str+="("
    
    print(sttr, r_str)
    return r_str

def is_ok_right_str(u):
    # u가 올바른 괄호 문자열인지? stck 써서 하면됨.
    
    if u == "": return True # 아마 이런경우는 없지 않을까 싶음

    stck = []
    for gwalho in u:
        print(gwalho)
        if gwalho == "(":
            stck.append("(")
        elif gwalho == ")":
            # stck에서 pop 해야함.
            if not stck: return False # pop 못하는 상황
            else: stck.pop() 
    
    if not stck: # stck 비어있다면 굿
        return True
    else: return False
    

def to_ok_gwalho_str(w):
    if w == "": return "" # 반환을 멀 해야할까?
    
    idx, l_cnt, r_cnt = 0, 0, 0
    for i in range(len(w)):
        if w[i] == "(": l_cnt+=1
        elif w[i] == ")": r_cnt+=1
        
        if l_cnt == r_cnt:
            idx=i
            break
    u, v = w[:idx+1], w[idx+1:]
    print("u, v는: ", u, v)
    flag = is_ok_right_str(u)
    print("flag는: ", flag)
    
    if flag: # u는 올바른 괄호 문자열
        sttr = to_ok_gwalho_str(v)
        return u + sttr
    
    else: # u는 올바르지 않아서 리팩토링 해야함.
        n_str = "(" + to_ok_gwalho_str(v) + ")"
        print("새로운 str: ", n_str)
        # r_n_str = reverse_gwalho(n_str)
        # 이게 아리나 u를 뒤집는거인듯
        r_n_u_str = reverse_gwalho(u[1:-1])
        
        return n_str + r_n_u_str


def solution(p):
    answer = ''
    flg = is_ok_right_str(p)
    print(flg)
    if flg:
        return p
    a = to_ok_gwalho_str(p)
    print(a)
    return a