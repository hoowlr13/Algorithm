N = int(input())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]

while True:
    a, b = list(map(int, input().split()))
    if (a and b) == -1:
        break
    else:
        graph[a][b] = 1
        graph[b][a] = 1

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


# graph의 가장 큰 값을 점수로 설정
answer = float('inf')
people = []
for i, data in enumerate(graph[1:], start=1):
    score = max(0 if x == float('inf') else x for x in data[1:])
    # 로직은 회장후보가 최솟값일때 1. 새 배열로 초기화 2. 회장후보 등록하기
    # 코드 개더럽네
    graph[i] = score
    if graph[i] <= answer: # 새로운 최솟값이 나타난 경우
        if graph[i] < answer:
            people = [] # 회장후보 초기화후 입력
        people.append(i)
    answer = min(answer, graph[i]) # 새 최솟값 설정하기 
    
people.sort()
print(answer,len(people))
print(*people)