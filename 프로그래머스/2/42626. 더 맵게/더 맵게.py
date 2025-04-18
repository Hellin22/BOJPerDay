import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 최소 힙으로 변환
    mix_count = 0

    while scoville:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return mix_count
        if not scoville:  # 더 섞을 음식이 없다면 실패
            return -1
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + (min2 * 2)
        heapq.heappush(scoville, new_scoville)
        mix_count += 1

    return -1  # 모든 경우 실패
