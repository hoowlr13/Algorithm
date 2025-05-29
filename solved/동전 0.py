N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
used = 0
for i in coins:
    while i <= K:
        K -= i
        used +=1
    
print(used)