city = int(input())
bus = int(input())
graph = [[float('inf')] * (city + 1) for _ in range( city+1)]
for i in range(1, bus+1):
    nowCity, arriveCity, value = list(map(int, input().split()))
    graph[nowCity][arriveCity] = min(value, graph[nowCity][arriveCity])
# 다시 원래방향으로 갈수있는 버스가 없음, 더 높은 value가 들어올 경우 min계산 

for k in range(1, city+1):
    graph[k][k] = 0 # 같은도시 제외
    for i in range(1, city+1):
        for j in range(1, city+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, city+1):
    # 모든 경로 계산후 갈수있는 경로가 없을때 inf대신 0으로 출력
    result = graph[i][1:]
    for r in result:
        if r == float('inf'):
            print(0, end=" ")
        else:
            print(r, end=" ")
    print()
