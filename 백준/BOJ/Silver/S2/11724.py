# 11724 _ 다시시도 해보기
# 연결요소
import sys

sys.setrecursionlimit(10**7)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1, n + 1):
    if not visited[i]:
        result += 1
        dfs(i)
print(result)
