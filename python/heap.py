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

# ===== #2
import heapq

def solution(jobs):
    tasks = sorted([(x[1], x[0]) for x in jobs],
                   key=lambda x: (x[1], x[0]), reverse=True)
    q = []
    heapq.heappush(q, tasks.pop())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[-1][1] <= current_time:
            heapq.heappush(q, tasks.pop())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.pop())
    return total_response_time // len(jobs)