repeat = int(input())
stack = []
for i in range(repeat):
    N = list(map(str, input().split()))
    if N[0] == "push":
        stack.append(int(N[1]))
    elif N[0] == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif N[0] == "size":
        print(len(stack))
    elif N[0] == "empty":
        if not stack:
            print("1")
        else:
            print("0")
    elif N[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print("-1")

