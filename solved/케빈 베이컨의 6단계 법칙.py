N, M = list(map(int, input().split())) # 유저수, 친구 관계의 수             
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i in range(M): # 관계설정
    a, b = list(map(int, input().split()))
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, N+1): # 경유지
    for i in range(1, N+1): # 출발지
        for j in range(1, N+1): # 도착지
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # 직선값과 경유값을 비교

answer = [float('inf'), float('inf')] # 사람과 숫자를 저장

for i in range(1, N+1):
    check = 0
    for j in range(1, N+1):
        check += graph[i][j]
    
    if answer[1] > check:
        answer = [i, check]
print(answer[0])