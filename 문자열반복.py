N = int(input())
for _ in range(N):
    repeat, S = input().split()

    for s in S:
        for i in range(int(repeat)):
            print(f"{s}",end="")
    print()