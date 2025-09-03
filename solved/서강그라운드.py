INF = float('inf')
n, m, r = map(int, input().split()) # area 갯수
graph = [[INF] * (n+1) for _ in range(n+1)]
items = list(map(int, input().split()))
for i in range(1, r+1):
    start, end, length = list(map(int, input().split())) # 시작, 끝, 수색길이 , 양방향 이동 가능, 중복x
    graph[start][end] = length
    graph[end][start] = length

for i in range(1, n+1):
    graph[i][i] = 0
    graph[i][i] = 0

for k in range(1, n+1): # 중간점
    for i in range(1, n+1):
        for j in range(1, n+1):
            # if (graph[i][k] + graph[k][j]) <= m and graph[i][j] <= m: # i-j로 바로가는 값이 inf일때 오류가생김
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = 0
for i in range(1, n+1): # 여기서 아까 저장했던 items 불러와서 체크하기 
    check = 0
    for j in range(1, n+1):
        if graph[i][j] != float('inf') and graph[i][j] <= m: # i = j인 착륙지점도 포함, 입력받았을때 탐색범위 초과인것 제외
                check += items[j-1]
        
    answer = max(check, answer)

print(answer)