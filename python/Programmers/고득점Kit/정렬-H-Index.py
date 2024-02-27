def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    if len(citations) < 1 or citations.count(0) == len(citations):
        return 0

    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)

print(solution([3, 0, 6, 1, 5]))