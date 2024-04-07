# 2751
import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(input()))
for i in sorted(data):
    print(i)