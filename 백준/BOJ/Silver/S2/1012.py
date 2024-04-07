# 1012
# 다시시도 해보기
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(b, a):
    q = deque()
    q.append((b, a))
    graph[b][a] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] == 1:
                q.append((ny, nx))
                graph[ny][nx] = 0


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    result = 0

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for b in range(n):
        for a in range(m):
            if graph[b][a] == 1:
                BFS(b, a)
                result += 1
    print(result)