import sys
n = int(sys.stdin.readline().rstrip())
stack_list = []

for _ in range(n):
    data = sys.stdin.readline().rstrip().split()

    if data[0] == "push":
        stack_list.append(data[1])
    elif data[0] == "pop":
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list.pop())
    elif data[0] == "size":
        print(len(stack_list))
    elif data[0] == "empty":
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == "top":
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])