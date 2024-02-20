# 2667
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
size = []

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    elif graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        return True
    else:
        return False


result = 0
cnt = 0

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            size.append(cnt)
            result += 1
            cnt = 0

print(result)
size.sort()
for i in size:
    print(i)