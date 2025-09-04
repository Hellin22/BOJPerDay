def solution(p):
    '''
    균형잡힌 문자열: ( ) 개수가 같은것
    올바른 문자열: 짝이 모두 맞는 경우
    
    w를 균형잡힌 문자열 2개(u v)로 분할 -> how?
    u를 균형잡힌 문자열로 못만들 때까지
    
    1. u가 올바른 문자열? -> v에 대해서 1단계부터 진행 후 u+v return
    
    2. u가 올바른 문자열x -> (  + v에 대해 1단계부터 진행한거를 붙임 + )
        u의 첫번째 마지막을 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임.
        ( v재귀 ) + u[1:-1]을 뒤집은거
        return
        
    u v로 나뉘는 순간은 u에 대해서 도는데 짝이 맞지 않는 순간이 나오는 경우
    
    '''
    def good_string(sttr):
        # sttr이 올바른 괄호 문자열인지 확인하기
        i = 0
        l, r = 0, 0
        while i < len(sttr):
            if sttr[i] == "(":
                l+=1
            elif sttr[i] == ")":
                r+=1
            if l < r: return False
            i+=1
        return True
    
    def reverse_string(sttr):
        ns = ""
        for i in range(len(sttr)):
            if sttr[i] == ")":
                ns+="("
            else: ns+=")"
        
        return ns
        
    def recursive_start(sttr):
        if sttr == "": return sttr
        
        # 1. sttr을 보면서 균형잡히지 않을 때 까지 반복하며 u v로 나누기
        # u v로 나누는 방법은 u의 첫번째꺼의 개수가 더 적은 경우에 종료
        i = 0
        l, r = 0, 0
            
        while i < len(sttr):
            if sttr[i] == "(":
                l+=1
            elif sttr[i] == ")":
                r+=1
            i+=1
            if l == r: break
        
        # i-1 까지가 u 의미 sttr[:i] sttr[i:] u, v
        u, v = sttr[:i], sttr[i:]
        
        # 2. u가 올바른 문자열인지 확인하기
        if not good_string(u): # u가 잘못된 문자열이라면
            nv = recursive_start(v)
            nv = "(" + nv + ")"
            nu = reverse_string(u[1:-1])
            return nv+nu
        
        else: # u가 올바른 문자열이라면
            return u + recursive_start(v)
    
    return(recursive_start(p))
            