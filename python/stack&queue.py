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