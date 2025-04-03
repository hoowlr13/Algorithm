repeat = int(input())

if repeat > 0:
    N = list(input())
    length = len(N)

    for i in range(repeat-1):
        diff = list(input())
        for j in range(length):
            if N[j] != diff[j]:
                N[j] = '?'
        
    print(''.join(N))


    