# 다시시도 해보기
# 11047
n, k = map(int, input().split()) # k는 합
units = []

for i in range(n):
    a = int(input())
    if a <= k:
        units.append(a)
units.sort(reverse=True)

cnt = 0
for unit in units:
    if k//unit > 0:
        cnt += k//unit
        k %= unit
        if k == 0:
            break
    else:
        continue

print(cnt)