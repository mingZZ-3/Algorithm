# 11723
import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    arg = sys.stdin.readline().strip()
    if arg == 'all':
        s = set([i for i in range(1, 21)])
    elif arg == 'empty':
        s = set()
    else:
        cal, num = map(str, arg.split())
        num = int(num)
        if cal == 'add':
            s.add(num)
        elif cal == 'remove' and num in s:
            s.remove(num)
        elif cal == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif cal == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)