from collections import Counter
def solution(citations):
    # hindex는 0부터 시작해서 계속해서 늘려가기
    # 10000까지?
    citations.sort()
    
    hindex = 0
    max_index = citations[-1]
    nonmun = len(citations)
    ans = hindex # 최대 hindex 의미
    
    ct = Counter(citations)
    
    while hindex <= max_index:
        if hindex-1 in ct:
            nonmun -= ct[hindex-1]
        if nonmun >= hindex:
            ans = hindex
        
        hindex+=1
    return ans