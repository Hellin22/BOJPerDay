def solution(numbers, k):
    '''
    1. 오름차순 정렬
    2. 부분 수열의 원소 모두 포함해야함.
    3. 합은 k
    4. 길이 가장 짧아야함.
    5. 길이 같으면 시작 idx 작은걸로
    
    투포인터
    '''
    l, r = 0, 0
    summ = numbers[0]
    ans = []
    while l <= r and r < len(numbers):
        # 1. summ이 k보다 작다. -> r+1
        if summ <= k:
            if summ == k:
                ans.append((l, r))
            r+=1
            if r == len(numbers): break
            summ+=numbers[r]
        # 2. summ이 k보다 크다 -> l+1
        if summ > k:
            summ-=numbers[l]
            l+=1
    ans.sort(key = lambda x: (x[1]-x[0], x[0]))
    return ans[0]