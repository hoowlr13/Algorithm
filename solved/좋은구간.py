L = list(map(int, input().split()))
ints = list(map(int, input().split()))
ints = [0] + ints # 엣지케이스 -> 범위가 ints에 없을경우 생각
n = int(input())

lowInts = 0
highInts = 0
ints.sort()

if n in ints:
    print(0)
else:
    for i in range(len(ints)):
        if ints[i] > n: 
            lowInts = ints[i-1]
            highInts = ints[i]
            break
    cnt = 0
    for j in range(lowInts+1, n+1):
        for k in range(n, highInts):
            if j == k:
                continue
            cnt +=1
    print(cnt)     
