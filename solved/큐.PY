
que = []
repeat = int(input())
for i in range(repeat):
    N = list(map(str, input().split()))
    if N[0] == 'push':
        que.append(int(N[1]))
    elif N[0] == 'pop':
        if que:
            print(que[0])
            que.remove(que[0])
        else:
            print("-1")
    elif N[0] == 'size':
        print(len(que))
    elif N[0] == 'front':
        if que:
            print(que[0])
        else:
            print("-1")
    elif N[0] == 'back':
        if que:
            print(que[-1])
        else:
            print("-1")
    elif N[0] == 'empty':
        if not que:
            print("1")
        else:
            print("0")