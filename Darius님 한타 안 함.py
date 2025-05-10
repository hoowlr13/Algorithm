N = list(map(int, input().split("/")))
if N[0] + N[2] < N[1] or N[1] == 0:
    print("hasu")
else:
    print("gosu")