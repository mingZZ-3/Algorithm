# 5597
result = [i for i in range(1, 31)]

for _ in range(28):
    a = int(input())
    result.remove(a)

print(min(result))
print(max(result))