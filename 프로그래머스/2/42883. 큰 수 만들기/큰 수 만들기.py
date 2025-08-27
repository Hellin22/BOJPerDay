def solution(number, k):
    
    '''
    k개의 수를 제거했을 때 만들 수 있는 가장 큰 수
    1,000,000자리 -> 완탐은 불가능하다
    
    최대값을 알아야함. -> 최대값 기준으로 왼쪽의 작은값 삭제
    오른쪽의 작은 값 삭제
    
    최대값만 기준으로 하면 안되네
    i 기준 i+1보다 작은 값이면 삭제
    i와 i+1을 비교했을 때 작은거 삭제?
    
    9876 2는? -> 98임...
    i 기준 i+1보다 작은값이면 삭제
    끝까지 갔는데 k가 안채워지면 :k까지
    
    i기준으로 i+1보다 작으면 삭제 -> str로 진행?
    stack으로 하면 더 좋을듯
    '''
    
    stck = []
    for i in number:
        while stck and stck[-1] < int(i) and k > 0: 
            # i보다 i+1이 커서 i번째를 없애고 i+1을 넣은것
            stck.pop()
            k-=1
        stck.append(int(i))
    
    return "".join(map(str, stck[:-k] if k != 0 else stck))