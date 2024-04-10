nums = [i for i in range(1, 10001)]

def d(n):
    if n > 10000:
        return
    add_list = []
    add_list.append(n)
    for i in list(map(int, str(n))):
        add_list.append(i)
    result = sum(add_list)
    if nums.count(result) > 0:
        nums.remove(result)
        return d(result)
    return

for i in range(1, 10001):
    if nums.count(i) > 0:
        d(i)

for i in nums:
    print(i)