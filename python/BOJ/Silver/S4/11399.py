# 11399
n = int(input())
p = list(map(int, input().split()))
p.sort()
tmp = 0
result = 0

for i in p:
    tmp += i
    result += tmp
print(result)