## 11403 - 경로찾기
# 인접행렬 형식
from collections import deque

INF = int(1e9)
n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            graph[i].append(j)

# 갈 수 있는 노드인지 확인
for k in range(n): # start
    for i in range(n): # 나를 포함한 모든 노드. end
        q = deque()
        visited = [False] * n
        positive = -1
        for j in graph[k]:
            q.append(j)

        while q:
            now = q.popleft()
            if now == i:
                positive = now
                break
            visited[now] = True
            for a in graph[now]:
                if not visited[a]:
                    q.append(a)

        if positive == -1:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()