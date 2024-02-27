from collections import deque

# 상, 하, 좌, 우 탐색을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, grid):
    queue = deque([(x, y)])
    # 현재 위치를 방문했다고 표시
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        print(f"방문 위치: ({x}, {y})")

        # 현재 위치에서 인접한 위치 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 배열 범위 안에 있고 방문하지 않았다면 큐에 넣고 탐색
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == 1:
                queue.append((nx, ny))
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
bfs(0, 0, visited, grid)

#####################################################################
################################ BFS ################################

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑음
        v = queue.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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
bfs(graph, 1, visited)