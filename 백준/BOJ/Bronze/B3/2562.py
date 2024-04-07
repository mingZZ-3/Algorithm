# 2562
data = []
for _ in range(9):
    tmp = int(input())
    data.append(tmp)
print(max(data))
print(data.index(max(data))+1)