### 프로그래머스
### 해시
# ===== #1
def hash_solution1(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
    for com in completion:
        temp -= hash(com)

    answer = dic[temp]
    return answer

a = hash_solution1(["leo", "kiki", "eden"], ["eden", "kiki"])
print(a)
# ===== #2

# ===== #3


# ===== #4
