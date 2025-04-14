'''
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

'''
def solution(clothes):
    dt = dict()
    for val, key in clothes:
        dt[key] = dt.get(key, 0)+1
    
    ans = 1
    for k, v in dt.items():
        ans *= (v+1)
    
    return ans-1