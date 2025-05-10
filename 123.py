import sys
input = sys.stdin.readline

N, M= map(int,input().split())
A=[int(input()) for i in range(N)]
A.sort()

for i in range(M):
    num=int(input())
    nums=N

    start, end = 0, N-1
    while start <= end:
        mid=(start+end) // 2

        if A[mid] < num: start = mid + 1
        elif A[mid]==num: 
            nums=min(nums,mid)
            end=mid-1
        else: end=mid-1

    print(-1 if nums>=N else nums)