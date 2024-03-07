# 다시시도 해보기
def solution(n, results):
    result = 0
    graph = [[-1] * (n + 1) for _ in range(n + 1)]

    for i in results:
        a, b = i[0], i[1]
        # a -이김-> b
        graph[a][b] = 1  # 이김
        graph[b][a] = 0  # 짐

    # 플로이드 워셜
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k] == graph[k][b] == 1:
                    graph[a][b] = 1
                    graph[b][a] = graph[k][a] = graph[b][k] = 0

    # 결과 도출
    for i in range(1, n + 1):
        if graph[i][1:].count(-1) == 1:
            result += 1

    return result