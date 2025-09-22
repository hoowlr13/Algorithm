N = int(input())
M = int(input())

graph = [[float('inf')] * (N + 1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # A가 B보다 무겁고 B에서 A로만 갈 수 있다.
    graph[b][a] = 1
    # graph[a][b] = 1

for i in range(N+1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])



for i in range(1, N + 1):
    ans = 0
    for j in range(1, N + 1):
        # 최단거리는 알고리즘으로 찾았으니 i -j, j -i두개를 확인해서 둘중 하나라도 inf라면 판별불가
        if graph[j][i] == float('inf') and graph[i][j] == float('inf'):
            ans +=1

    print(ans)