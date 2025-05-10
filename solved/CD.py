
while True:
    N, M = list(map(int, input().split()))
    if N == 0 and M == 0:
        break
    
    nCnt = set([int(input()) for _ in range(N)])
    mCnt = set([int(input()) for _ in range(M)])

    print(len(mCnt & nCnt))
# 이분탐색으로 다시시도
"""
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
nCnt = []
mCnt = []
for _ in range(N):
    nCnt.append(int(input()))
for _ in range(M):
    mCnt.append(int(input()))

x = list(map(int, input().split()))

cnt = 0
for i in nCnt:
    low = 0
    high = len(mCnt) -1

    while low <= high:
        mid = (low + high) // 2    
        if i == mCnt[mid]:
            cnt +=1 
            break
        elif i > mCnt[mid]: 
            low = mid +1
        else:
            high = mid -1 

print(cnt)



"""