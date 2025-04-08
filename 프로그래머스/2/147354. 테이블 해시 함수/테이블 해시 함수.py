'''
data	                            col  row_begin	row_end	 result
[[2,2,6],[1,5,10],[4,2,9],[3,8,3]]	 2	     2	       3	   4

[[2,2,6],
[1,5,10],
[4,2,9],
[3,8,3]]

즉, row들에 대해서 1. row[col] 오름차순 정렬, 2. row[0] 내림차순 정렬
그러면 정렬된 튜플이 나올것.
S_i를 i번째 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합.
즉, S_1은 첫번째 튜플에 대햇 각 컬럼을 i로 나눔.

row_begin <= i <= row_end인 모든 S_i를 누적해서 xor 한 값을 가져와라.

'''

def solution(data, col, row_begin, row_end):
    answer = 0
    
    # data를 sort 해야함.
    data.sort(key = lambda x: (x[col-1], -x[0])) # row[col] 오름, row[0] 내림(-연산)
    
    llist = []
    answer = 0
    for i in range(row_begin-1, row_end+1-1):
        
        namerji_sum = 0
        for j in range(len(data[i])):  
            # data[i] # row가 나옴.
            namerji_sum += data[i][j] % (i+1)
            # data[i][j]를 각각 i로 나눈 나머지를 더함.
            # i+1로 나눠야한다.
        # 이거랑 이전꺼를 xor 해야함.
        answer = answer^namerji_sum        
    
            
        
    
    return answer