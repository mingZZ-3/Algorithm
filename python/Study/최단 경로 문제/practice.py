#################################
### 1 - 전보 : 우선순위 큐
import heapq

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

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
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에 y번 노드로 가는 비용 z
    graph[x].append((y, z))

dijkstra(c)

cnt = 0 # 도달할 수 있는 노드의 개수
max_distance = 0 # 가장 멀리 있는 노드와의 최단 거리
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        cnt += 1
        max_distance = max(d, max_distance)

# 시작 노드는 제외해야 하므로 cnt - 1
print(cnt-1, max_distance)


#################################
### 2 - 미래 도시
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF]*(n + 1) for _ in range(n + 1)]

for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visit, end = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][visit] + graph[visit][end]

if distance >= INF:
    print(-1)
else:
    print(distance)