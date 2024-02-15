# 2839 - 설탕 배달
sugar = int(input())
bags = 0

while sugar > 0:
    if sugar % 5 == 0:
        bags += (sugar // 5)
        break
    sugar -= 3
    bags += 1
else:
    bags = -1

print(bags)