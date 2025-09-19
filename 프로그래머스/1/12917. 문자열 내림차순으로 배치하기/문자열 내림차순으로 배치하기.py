def solution(s):
    return "".join(sorted(list(s), key = lambda x: -ord(x)))