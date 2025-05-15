T = int(input())
for i in range(T):
    N = int(input())
    answer = 0
    for i in range(1, N + 1):
        if N - i < 0:
            break
        else:
            N -= i
            answer +=1

    print(answer)