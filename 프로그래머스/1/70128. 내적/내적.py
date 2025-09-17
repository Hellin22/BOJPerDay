def solution(a, b):
    ans = 0
    for aa, bb in zip(a, b):
        ans += aa*bb
    return ans