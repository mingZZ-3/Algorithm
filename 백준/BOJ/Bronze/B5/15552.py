# 15552
import sys

n = int(sys.stdin.readline())

for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    if a < 1 or b < 1 :
        continue
    else :
        print(a + b)