N = [int(input()) for _ in range(10)]
check = [False] * 1001
for i in N:
    cnt = i % 42
    check[cnt] = True
print(sum(check))
