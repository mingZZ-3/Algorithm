# 1 - 떡볶이 떡 만들기
# 시간 복잡도 : O(N)
import bisect


def rice_mid(array, length, cut_len):
    result = 0
    for i in array:
        if i > cut_len:
            result += (i - cut_len)

    if result == length:
        return cut_len
    else:
        return rice_mid(array, length, cut_len - 1)


n, m = map(int, input().split())
rice = list(map(int, input().split()))
rice.sort()
print(rice_mid(rice, m, rice[-1]))

# 1 --> 이진 탐색으로 풀기 (while)
n, m = map(int, input().split())
rice = list(map(int, input().split()))

start = 0
end = max(rice)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in rice:
        if x > m:
            total += x - m

    if total < m:
        end = mid - 1
    else:
        result = mid
        right = mid + 1

print(result)

# 2 - 정렬된 배열에서 특정 수의 개수 구하기
def count_by_range(a, left_value, right_value):
    left_index = bisect.bisect_left(a, left_value)
    right_index = bisect.bisect_right(a, right_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

cnt = count_by_range(array, x, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)