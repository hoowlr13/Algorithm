# 그래프를 일방통행으로만 그리면 되는거지 모든 정점과 연결되어있으며 자신의 키를 확인가능하다
N, M = list(map(int, input().split())) # 학생수, 키 비교 횟수 

graph = [[float('inf')] * (N+1) for _ in range(N+1)] # 0제외
for _ in range(M):
    a, b = list(map(int, input().split())) # a가 b보다 무조건 키가 작다 
    graph[a][b] = 1

# 키 순서는 출력하지않아도 괜찮기에 통과가능하다 라고만 알려주면 됨
for i in range(1, N+1):
    graph[i][i] = 0

# 알고리즘 수행중 다른 조건은 빼버리기
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            


# 그래프 돌면서 다 채워져있는지 확인하기
answer = N
for i in range(1, N+1):
    for j in range(1, N+1):
        # 만약 i->j, j->i모두 inf(차이를 파악할 수 없음) 상태라면 정답에서 빼기
        if graph[i][j] == float('inf') and graph[j][i] == float('inf'):
            answer -=1
            break

print(answer)

        
            