# 1916 - 최소비용 구하기 (최단 경로, 우선순위 큐)
import sys, heapq

INF = int(1e9)
n = int(sys.stdin.readline())  # 노드
m = int(sys.stdin.readline())  # 간선

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(distance[end])