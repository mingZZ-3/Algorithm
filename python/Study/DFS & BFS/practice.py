# 1 - 음료수 얼려 먹기 (DFS)
def dfs(x, y):
    # 주어진 범위를 넘어가는 경우
    if  x < 0 or x >= n or y < 0 or y >= m:
        return False
    elif graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y) # 상
        dfs(x + 1, y) # 하
        dfs(x, y - 1) # 좌
        dfs(x, y + 1) # 우
        return True
    else:
        return False

n , m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

# 2 - 미로 탈출
from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 현재위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


n , m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우 탐색을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))
for i in range(n):
    print(graph[i])