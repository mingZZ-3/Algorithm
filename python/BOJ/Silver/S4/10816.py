# 1920
import bisect
import sys


def count_by_range(a, value):
    left_index = bisect.bisect_left(a, value)
    right_index = bisect.bisect_right(a, value)
    return right_index - left_index


n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for i in targets:
    print(count_by_range(array, i), end=" ")