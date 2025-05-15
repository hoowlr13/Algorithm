"""어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 
대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 
0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 
단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다."""

from collections import deque



def bfs(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cnt = 0

    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) :
                if (nx, ny) not in visited:
                    
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return 


if __name__ == "__main__":
    X, Y = list(map(int, input().split()))
    grid = []
    for i in range(X):
        grid.append([])
        N = list(map(int, input().split()))
        for j in range(len(N)):    
            grid[i].append(N[j])
    
    print(bfs(0, 0, grid))

# 그리드에서 전체넓이 탐색 -> 이중에서 우선순위를 만든다? 1인걸 먼저 탐색하고 아니면 0 을 탐색하는 방법을 사용한다.
# 1이없다면 전부탐색이 되는거고 1이있다면 1빼고 다른건 탐색하지않음 