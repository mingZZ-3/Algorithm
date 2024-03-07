import heapq

def solution(n, edges):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    q = []
    distance[0] = 0
    distance[1] = 0
    heapq.heappush(q, (0, 1))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    return distance.count(max(distance))