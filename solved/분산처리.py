repeat = int(input())
for _ in range(repeat):
    N, M = list(map(int, input().split()))
    if not N % 10:
        print("10")
    else:
        cnt = N
        for i in range(M-1):
            cnt %= 10
            cnt *= N
        print(cnt%10)    