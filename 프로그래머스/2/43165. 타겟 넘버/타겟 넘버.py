from collections import deque

def solution(numbers, target):
    cnt = 0
    n = len(numbers)
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    
    while queue:
        tmp, idx = queue.popleft()
        idx += 1
        if idx < n: # 계산할 값이 남음
            queue.append([tmp + numbers[idx], idx])
            queue.append([tmp - numbers[idx], idx])
        else: # 계산할 값이 없음
            if tmp == target:
                cnt += 1
    return cnt