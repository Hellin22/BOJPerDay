'''
[[1, 4], 
[3, 2], 
[4, 1]]

[[3, 3], 
[3, 3]]

'''

def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        llist = []
        for k in range(len(arr2[0])):
            a = 0
            for j in range(len(arr1[i])):
                a += arr1[i][j] * arr2[j][k]   
            llist.append(a)
        answer.append(llist)
            
    return answer