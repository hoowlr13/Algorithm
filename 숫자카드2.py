from bisect import bisect_left, bisect_right
_ = int(input())
N = list(map(int, input().split()))
N.sort()
_ = int(input())
M = list(map(int, input().split()))
for i in M:
    left = bisect_left(N, i)
    right = bisect_right(N,i)
    if (right - left) >= 0:
        print(right-left, end=" ")
    