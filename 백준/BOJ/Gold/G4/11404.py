# 11404 - 플로이드 워셜 (최단 경로)
import sys

INF = int(1e9)
n = int(sys.stdin.readline()) # 노드
m = int(sys.stdin.readline()) # 간선

graph = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    # x -z-> y
    graph[x-1][y-1] = min(z, graph[x-1][y-1])

# 플로이드 워셜 동작
for k in range(n): # 거치는 노드
    for a in range(n): # 시작 노드
        for b in range(n): # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("0", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()