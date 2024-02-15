# 2738
row, column = map(int, input().split())
A, B = [], []

# 행렬 만들기
for i in range(row):
    A.append(list(map(int, input().split())))

for i in range(row):
    B.append(list(map(int, input().split())))

for i in range(row):
    for j in range(column):
        print(A[i][j] + B[i][j], end=" ")
    print()