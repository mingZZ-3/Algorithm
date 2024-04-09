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
            a, b = map(int, jobs[i])
            if a <= now:
                wait_list.append([i, b])

        if len(wait_list) > 0:
            wait_list.sort(key = lambda x:x[1])
            time, length = map(int, jobs.pop(wait_list[0][0]))
            cnt += (now - time) + length
            now += length
        else:
            time, length = map(int, heapq.heappop(jobs))
            now = time
            cnt += (now - time) + length
            now += length

    return cnt//total