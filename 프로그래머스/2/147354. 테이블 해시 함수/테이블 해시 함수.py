def solution(data, col, row_begin, row_end):
    '''
    행은 튜플
    첫번째 컬럼은 기본키
    
    해시 함수는 col, row_begin, row_end 입력받음
    
    1. col 번째 컬럼 값 기준 오름차순. 동일? -> 첫번째 컬럼 값으로 내림차순
    2. 정렬한 후에 S_i는 i번째 튜플에 대해 각 컬럼을 i로 나눈 나머지들의 합
    3. row_begin <= i <= row_end인 모든 S_i를 누적해서 xor 연산(^)
    
    (row+1)로 %한 값의 합
    이때 row는 row_begin ~ row_end
    
    '''
    data.sort(key = lambda x: (x[col-1], -x[0]))
    s_i = 0
    for i in range(row_begin-1, row_end):
        summ = 0
        for j in range(len(data[i])):
            summ += data[i][j]%(i+1)

        s_i = s_i^summ
    return s_i

    