from collections import deque
import sys
sys.setrecursionlimit(10**4) 


N, M = list(map(int, input().split()))
graph = [[] for _ in range(N+1)] # 0제외 정점 + 1


for m in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (N+1)
visited[0] = True
answer = 1

def dfs (graph, v, visited):
    global answer
    visited[v] = True
    # print(f"이번 방문은{v}")
    for check in graph[v]:
        if not visited[check]:
            # print(f"방문안한{check} 이동")
            dfs(graph, check, visited)
    

dfs(graph, 1, visited)
while False in visited: # 연결안된거 찾기
    not_visit = visited.index(False)
    dfs(graph, not_visit, visited)
    answer +=1

print(answer)
