N, K = list(map(int, input().split()))
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    a, b = list(map(int, input().split())) # a-> b로 간다 
    graph[a][b] = 1

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
search = int(input())
for _ in range(search):
    a, b = list(map(int, input().split())) # find a, b
    
    if graph[a][b] != float('inf'): # a -> b경로가 있다면?
        print(-1)
    elif graph[b][a] != float('inf'):
        print(1)
    else:
        print(0) 