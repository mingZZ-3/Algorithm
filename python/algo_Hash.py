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

# ===== #2
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for num in phone_number:
            temp += num
            if temp in hash_map and temp != phone_number:
                return False
    return True

# ===== #3
def solution(clothes):
    from collections import Counter
    from functools import reduce

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1

    return answer

# ===== #4
