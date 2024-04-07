# 2178 - 최소의 칸 --> bfs
from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif not visited[nx][ny] and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True
            else:
                continue
    return graph[n-1][m-1]

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(bfs(0,0))