while True:
    N = list(map(int, input().split()))
    if all(x == 0 for x in N):
        break
    N.sort()
    if (N[-1] * N[-1]) == (N[0] * N[0] + N[1] * N[1]):
        print("right")
    else:
        print("wrong")