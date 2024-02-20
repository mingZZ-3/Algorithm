# 2606
from collections import deque


def dfs(g, v, visit):
    visit[v] = True
    for i in g[v]:
        if not visit[i]:
            dfs(g, i, visit)


def bfs(g, v, visit):
    queue = deque([v])
    visit[v] = True
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


computers = int(input())
line = int(input())

visited = [False] * (computers + 1)
graph = [[] for _ in range(computers + 1)]
for i in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited)
print(visited.count(True) - 1)