# 1110
n = int(input())

new = n
cnt = 0

while True:
    sum = 0
    for i in str(new):
        sum += int(i)
    new = str(new)[-1] + str(sum)[-1]
    cnt += 1

    if n == int(new):
        break
print(cnt)