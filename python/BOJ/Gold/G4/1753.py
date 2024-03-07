# 1753 최단 경로
import heapq, sys

INF = int(1e9)
node,line = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = [[] for _ in range(node + 1)]
distance = [INF] * (node + 1)

for i in range(line):
    x, y, z = map(int, sys.stdin.readline().split())
    # x -z-> y
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, node + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])