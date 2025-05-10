import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M = list(map(int, input().split()))
nCnt = []
mCnt = []
for _ in range(N):
    nCnt.append(int(input()))
for _ in range(M):
    mCnt.append(int(input()))
nCnt.sort()

cntDict = {}
for i, value in enumerate(nCnt):
    if not value in cntDict:
        cntDict[value] = i

for m in mCnt:
    if m in cntDict:
        print(f"{str(cntDict[m])}\n")
    else:
        print("-1\n")



"""import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M = list(map(int, input().split()))
nCnt = []
mCnt = []
for _ in range(N):
    nCnt.append(int(input()))
for _ in range(M):
    mCnt.append(int(input()))


nCnt.sort()
cnt = 0
for m in mCnt:
    low = 0
    high = len(nCnt) -1
    answer = len(nCnt)+1

    while low <= high:
        mid = (low + high) // 2    
        if m == nCnt[mid]:
            while mid > 0 and nCnt[mid-1] == m:
                mid -=1
            print(f"{mid}\n")
            break
        elif m > nCnt[mid]: 
            low = mid +1
        else:
            high = mid -1 
    else:
        print("-1\n")
"""