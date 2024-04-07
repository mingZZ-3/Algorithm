# 2475
def cal(data):
    result = 0
    for i in data:
        result += i*i
    print(result % 10)

n = list(map(int, input().split()))
cal(n)