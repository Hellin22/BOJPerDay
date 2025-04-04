'''
투포인터 쓰면 될라나?
left, right = 0
while true:
    현재 합이 k보다 작다 = right+=1 (right는 idx임)
        현재 합 구하기
    현재 합이 k보다 크다 = left+=1
        현재 합 구하기
    현재 합이 k다 = right+=1 (추가해줘야함.)
        현재 합 구하기
'''

def solution(sequence, k):
    answer = []
    left, right = 0, 0
    summ = sequence[left]
    while True:
        if summ < k:
            right+=1
            if right == len(sequence): break
            summ+=sequence[right]
        elif summ > k:
            summ-=sequence[left]
            left+=1
        else:
            answer.append((right-left+1, left, right))
            right+=1
            if right == len(sequence): break
            summ+=sequence[right]
        if left> right: break
        if left == len(sequence): break
    
    return [sorted(answer)[0][1], sorted(answer)[0][2]]