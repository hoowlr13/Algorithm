from collections import deque
import sys
print = sys.stdout.writelines
sys.setrecursionlimit(10**4) # 10^6은 메모리초과 


N, M, V = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)] # 정점 갯수 + 1을 사용 -> 0제외
for i in range(M):
	one, two = list(map(int, input().split())) 
	graph[one].append(two) # 1과 연결된 2를 추가
	graph[two].append(one) # 2와 연결된 1 추가 -> 양방향 이동가능

# 순서 정렬
for g in range(len(graph)):
	graph[g].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(f"{v} ")
    for i in graph[v]: # 이차원배열 v와 연결된 모든 점들을 탐색
    	if not visited[i]: # 만약 i가 있다면? 아래로 내려가기 
        	dfs(graph, i, visited)
			
    
def bfs(graph, v, visited):
	print("\n")
	visited[v] = True
	aftervisit.append(v)
    
	while aftervisit:
		q = aftervisit.popleft()
		print(f"{q} ")

		for i in graph[q]:
			if not visited[i]:
				aftervisit.append(i)
				visited[i] = True	
		
	


visited = [False] * (N + 1)
dfs(graph, V, visited)


visited = [False] * (N + 1)
aftervisit = deque()

bfs(graph, V, visited)
	
