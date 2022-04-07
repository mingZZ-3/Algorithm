# ===== #1
def solution(id_list, report, k):
    answer = []
    a = list(set(report))
    dictionary2 = {name : 0 for name in id_list}
    dictionary = {name : [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer

# ===== #2
def solution(id_list, report, k):
    answer = []
    a = list(set(report))
    dictionary2 = {name : 0 for name in id_list}
    dictionary = {name : [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer