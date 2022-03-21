### 프로그래머스
### 스택/큐
# ===== #1
from math import ceil

def solution(progresses, speeds):
    cnt = 1
    answer = []

    ## 필요한 작업일 리스트 생성
    work_date = list(map(lambda x: (ceil((100-progresses[x])/speeds[x])), range(len(progresses))))

    ## 배포 일정
    for i in range(len(work_date)):
        try:
            if work_date[i] >= work_date[i+1]:
                cnt += 1
                work_date[i+1] = work_date[i]
            else:
                answer.append(cnt)
                cnt = 1
        except IndexError:
            answer.append(cnt)

    return answer

# ===== #2
def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    cnt = 0

    while True:
        try:
            tmp = queue.pop(0)
            if any(tmp[1] < q[1] for q in queue):
                queue.append(tmp)
            else:
                cnt += 1
                if tmp[0] == location:
                    break
        except IndexError:
            break
    return cnt

# ===== #3
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weight):
    bridge = []
    tmp = 0
    time = 0
    weightOnBridge = 0

    while True:
        try:
            tmp = truck_weight.pop(0)

            if (tmp+weightOnBridge) <= weight:
                bridge.append(tmp)
                weightOnBridge += tmp

            ##else:


        except IndexError:
            continue

def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec

# ===== #4
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer