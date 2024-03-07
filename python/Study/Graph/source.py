#####################################
### 서로소 집합

# 특정 원소가 속한 집합 찾기
def find_parend(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parend(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parend(parent, a)
    b = find_parend(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=" ")
for i in range(1, v + 1):
    print(find_parend(parent, i), end=" ")
print()
# 부모 테이블 내용 출력하기
print('부모 테이블: ', end=" ")
for i in range(1, v + 1):
    print(parent[i], end=" ")


#####################################
### 서로소 집합 - 사이클

# 특정 원소가 속한 집합 찾기
def find_parend(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parend(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parend(parent, a)
    b = find_parend(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parend(parent, a) == find_parend(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("cycle")
else:
    print(-1)


#####################################
### 크루스칼 알고리즘

# 특정 원소가 속한 집합 찾기
def find_parend(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parend(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parend(parent, a)
    b = find_parend(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 튜플의 첫번째 원소를 기준으로 sort함
    edges.append((cost, a, b))
edges.sort()

for i in edges:
    cost, a, b = i
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parend(a) != find_parend(b):
        union_parent(parent, a, b)
        result += cost
print(result)


#####################################
### 위상 정렬
from collections import deque

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=" ")


topology_sort()