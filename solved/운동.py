V, E = list(map(int, input().split()))
graph = [[float('inf')] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = list(map(int, input().split()))
    graph[a][b] = c # 일방통행 도로이다.

for i in range(1, V+1):
    graph[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = float('inf')
for i in range(1, V+1):
    for j in range(1, V+1):
        if not i == j: # 자기자신이 아닐경우
            check = graph[i][j] + graph[j][i] # a->b b->a로 가장 작은 수를 찾음
            ans = min(ans, check)

# ans를 못찾았을경우 - inf일때는 -1출력
if ans == float('inf'):
    print(-1)
else:
    print(ans)