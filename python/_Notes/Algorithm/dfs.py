# 상, 하, 좌, 우 탐색을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_stack(x, y, visited, grid):
    stack = [(x, y)]
    # 현재 위치를 방문했다고 표시
    visited[x][y] = True

    while stack:
        x, y = stack.pop()
        print(f"방문 위치: ({x}, {y})")

        # 현재 위치에서 인접한 위치 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 배열 범위 안에 있고 방문하지 않았다면 스택에 넣고 탐색
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == 1:
                stack.append((nx, ny))
                visited[nx][ny] = True

# 2차원 배열 예제 (1은 갈 수 있는 경로, 0은 갈 수 없는 경로)
grid = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
]

# 방문 정보
visited = [[False] * len(grid[0]) for _ in range(len(grid))]

# 예시로 (0, 0)부터 탐색 시작
dfs_stack(0, 0, visited, grid)

#####################################################################
################################ DFS ################################

def dfs(graph, v, visited) :
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)