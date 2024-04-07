# 2252 - 줄 세우기 (위상 정렬)
from collections import deque

v, e = map(int, input().split())
edges = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)

for i in range(e):
    a, b = map(int, input().split())
    # a -> b
    edges[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in edges[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=" ")

topology_sort()