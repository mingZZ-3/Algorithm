# 1920
import sys


def binary_search(a, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if a[mid] == target:
        return 1
    elif a[mid] > target:
        return binary_search(a, target, start, mid - 1)
    else:
        return binary_search(a, target, mid + 1, end)


n = int(input())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
m = int(input())
targets = list(map(int, sys.stdin.readline().split()))

for i in targets:
    print(binary_search(array, i, 0, n-1))