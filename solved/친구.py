"""
입력
3
NYY
YNY
YYN

1 line -> 1과 1은 친구가 x 1과 2는 친구가 o 1과 3은 친구가 o
2 line -> 2과 1은 친구가 o 2과 2는 친구가 x 2과 3은 친구가 o 
"""
inf = float('inf')
N = int(input())
graph = [[inf] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i in range(1, N+1):
    friend = input()
    for j in range(1, N+1):
        if friend[j-1] == 'Y':
            graph[i][j] = 1
            graph[j][i] = 1
        # elif friend[j-1] == 'N': # NO일 경우
        #     graph[i][j] = 0
        #     graph[j][i] = 0
            


for k in range(1, N+1): # 중간점
    for i in range(1, N+1): # 시작점
        for j in range(1, N+1): # 도착점
            graph[i][j] = min(graph[i][j], (graph[i][k] + graph[k][j]))


answer = [0, 0] # 사람, 2-친구
for i in range(1, N+1):
    check = 0
    for j in range(1, N+1):
        if i != j and graph[i][j] < 3: # 동일 인물이 아니고  | i - j가 친구거나 i - k - j가 친구일 경우 -> 3미만
            check +=1
    
    if answer[1] < check:
        answer = [i, check]
print(answer[1])

