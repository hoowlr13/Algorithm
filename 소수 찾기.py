
repeat = int(input())
N = list(map(int, input().split()))
cnt = 0
for n in N:
    if n < 2:
        continue
    if not any(n % x == 0 for x in range(2, n)):
        cnt+=1

print(cnt)