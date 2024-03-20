# 10431
import sys

def bubble_sort(array):
    global cnt
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                cnt += 1


n = int(sys.stdin.readline())
for i in range(1, n + 1):
    data = list(map(int, sys.stdin.readline().strip().split()))
    t = data[0]
    students = data[1:]

    cnt = 0
    bubble_sort(students)
    print(i, cnt)