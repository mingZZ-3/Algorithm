import heapq


def solution(jobs):
    total = len(jobs)
    heapq.heapify(jobs)

    # 현재 시간, 작업 시간
    now, cnt = map(int, jobs.pop(0))
    now += cnt
    while jobs:
        wait_list = []
        for i in range(len(jobs)):
            time, length = map(int, jobs[i])
            if time <= now:
                wait_list.append([i, length])

        if len(wait_list) == 1:
            time, length = map(int, jobs.pop(wait_list[0][0]))
            cnt += (now - time) + length
            now += length
        elif len(wait_list) > 0:
            # 작업 가능한 것 중 시간이 가장 짧은 것 하나 실행
            wait_list.sort(key = lambda x:x[1])
            time, length = map(int, jobs.pop(wait_list[0][0]))
            cnt += (now - time) + length
            now += length
        else:
            # 현재 작업 가능한 것이 없는 경우,
            # 가장 먼저 있는 작업을 실행
            time, length = map(int, heapq.heappop(jobs))
            now = time
            cnt += (now - time) + length
            now += length

    return cnt//total

print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))