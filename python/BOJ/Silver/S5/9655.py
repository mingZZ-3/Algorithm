# 9655
import sys

n = int(sys.stdin.readline())
cnt = 0

if n // 3 > 1:
    cnt = n//3 + n%3
else:
    cnt = n

if n % 2 == 0:
    print("CY")
else:
    print("SK")