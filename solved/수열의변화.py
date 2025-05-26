N, K = list(map(int, input().split()))
A = list(map(int, input().split(',')))
if K == 0:
    print(','.join(map(str, A)))
else:
    for i in range(K):
        new_A = []
        for j in range(len(A)-1):
            new_A.append(A[j+1]-A[j])
        
        A = new_A
    print(','.join(map(str, new_A)))
