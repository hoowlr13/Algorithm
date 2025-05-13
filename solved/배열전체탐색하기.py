from bisect import bisect_left, bisect_right
n, m = list(map(int, input().split()))
N = sorted(list(map(int, input().split())))
for i in range(m):
    check = list(map(int, input().split()))
    if check[0] == 1:
        print(f"{len(N) - bisect_left(N, check[1])}")
    elif check[0] == 2:
        print(f"{len(N) - bisect_right(N, check[1])}")
    elif check[0] == 3:
        print(f"{bisect_right(N, check[2]) - bisect_left(N, check[1])}")