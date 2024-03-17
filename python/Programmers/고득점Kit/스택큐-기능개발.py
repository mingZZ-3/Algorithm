# 스택/큐 - 기능개발
# 다시시도 해보기
def solution(progresses, speeds):
    result = []
    time = 0
    cnt = 0

    while len(progresses) > 0:
        x = progresses[0] + speeds[0]*time
        if x >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                result.append(cnt)
                cnt = 0
            time += 1
    result.append(cnt)
    return result


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))