from collections import deque
N, M = list(map(int, input().split()))
maze = []
for i in range(N):
    maze.append([])
    txt = input()
    for j in range(len(txt)):
        maze[i].append(int(txt[j]))

def grid_bfs(grid, start_row, start_col, end_row, end_col):
    cnt = 0
    rows, cols = len(grid), len(grid[0]) # 행,열 찾기 
    visited = set([(start_row, start_col)]) 
    queue = deque([(start_row, start_col, 1)]) 
   
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    while queue: # 큐가 있을때(없다면 모두 탐색한것)
        row, col, cnt = queue.popleft() # 큐에서 왼쪽을빼고 행, 열로 반환

        if row == end_row and col == end_col:
            return cnt

        for dr, dc in directions: # 좌우하상 탐색
            new_row, new_col = row + dr, col + dc #현재 행열에서 상하좌우 탐색하기위해 더함
                        
            # 그리드 범위 내에 있고, 방문하지 않았으며, 이동 가능한 위치인지 확인
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                (new_row, new_col) not in visited and grid[new_row][new_col] == 1):  
                
                queue.append((new_row, new_col, cnt + 1))   
                visited.add((new_row, new_col))
        
        
    
            
print(grid_bfs(maze, 0, 0, N-1, M-1)) 