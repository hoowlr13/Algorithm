from collections import deque
N, M = int(input().split())


def grid_bfs(grid, start_row, start_col):
    rows, cols = len(grid), len(grid[0]) # 행,열 찾기 
    visited = set([(start_row, start_col)]) # 방문했던곳 확인(set로 중복제거 and 시작지점 추가)
    queue = deque([(start_row, start_col)]) # 큐로 상하좌우를 전부반복한다
    
    # 상하좌우 이동 방향 왼쪽 오른쪽 아래 위쪽 순서로 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    while queue: # 큐가 있을때(없다면 모두 탐색한것)
        row, col = queue.popleft() # 큐에서 왼쪽을빼고 행, 열로 반환
        
        
        # 4방향 탐색
        for dr, dc in directions: # 좌우하상 탐색
            new_row, new_col = row + dr, col + dc #현재 행열에서 상하좌우 탐색하기위해 더함
                        
            # 그리드 범위 내에 있고, 방문하지 않았으며, 이동 가능한 위치인지 확인
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                (new_row, new_col) not in visited):  # '#'는 벽이라고 가정
                
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
            

# 이동하면 안되는 좌표를 확인한뒤에 다시 거기를 0 으로 바꾸면 끝 -> 이건 전 행열을 다시확인할수없어서 실패
