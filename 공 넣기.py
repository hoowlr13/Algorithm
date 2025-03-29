N, M = map(int, input().split())
basket = {c:0 for c in range(1, N+1)}
for i in range(M):
    fst, lst, cnt = map(int, input().split())
    for i in range(fst, lst+1):
        basket[i] = cnt
for key, value in basket.items():
    print(value, end=" ")        
