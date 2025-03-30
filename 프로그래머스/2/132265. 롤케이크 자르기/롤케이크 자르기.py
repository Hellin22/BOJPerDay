'''
topping은 1~십만의 숫자
topping의 길이는 1~십만
저기서 토핑의 개수가 동일하게 자르려면 어떻게 해야하는가??

일단 dict로 가는게 맞는거같음.
토핑 자체의 개수는 x -> 토핑의 종류 -> 결국 0과 -1부터 해야하는것.
-> 투포인터 하나로 left, mid, right(left~mid, mid+1 ~ right)
이 사이에 있는 토핑 종류만 체크하면 될듯?
그리고 길이가 1이면 못자른다 == 1일때 예외처리
'''

def solution(topping):
    answer = 0
    left, mid, right = 0, 0, len(topping)-1
    mid = 1
    n = len(topping)
    if right == 0:
        return answer
    # left, right도 의미가 없는거같네?
    dtLeft, dtRight = dict(), dict()
    for i in range(mid):
        dtLeft[topping[i]] = dtLeft.get(topping[i], 0)+1
    for i in range(mid, n):
        dtRight[topping[i]] = dtRight.get(topping[i], 0)+1
    
    while mid != n-1:
        if len(dtLeft) == len(dtRight): answer+=1
        dtLeft[topping[mid]] = dtLeft.get(topping[mid], 0)+1
        if dtRight[topping[mid]]-1 == 0:
            del dtRight[topping[mid]]
        else: dtRight[topping[mid]]-=1 
        mid+=1
    return answer