### 프로그래머스
### 스택/큐
# ===== #1
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        minimum = heapq.heappop(scoville)
        if minimum >= K:
            break
        if len(scoville) < 1:
            return -1
        secminimum = heapq.heappop(scoville)
        heapq.heappush(scoville, minimum + (secminimum * 2))
        answer += 1

    return answer
