# 다시시도 해보기
# 시간 초과
def solution(participant, completion):
    for i in range(len(completion)):
        participant.remove(completion[i])
    return participant[0]

import collections
def solution(participant, completion):
    answer = (collections.Counter(participant)
              - collections.Counter(completion))
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))