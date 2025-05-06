def solution(arr):
    answer = []
    minn = float("INF");
    minn_idx = 0
    for i, val in enumerate(arr):
        if val < minn:
            minn = val
            minn_idx = i
    print(minn, minn_idx)
    
    if len(arr) == 1:
        return [-1]
    return arr[:minn_idx] + arr[minn_idx+1:]
