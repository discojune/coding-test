from collections import deque

def bfs(block_coord, land, land_max, visited, cluster_map, cluster_idx):
    queue = deque()
    
    block_y = block_coord[0]
    block_x = block_coord[1]
    
    queue.append((block_y, block_x))
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    land_width_m = land_max[0]
    land_height_n = land_max[1]
    
    petro_amount = 0
    while queue:
        y, x = queue.popleft()

        cluster_map[y][x] = cluster_idx
        
        petro_amount += 1
        
        for move in moves:
            next_x = x + move[1]
            next_y = y + move[0]
            
            
            if next_x < 0 or next_y < 0 or next_x >= land_width_m or next_y >= land_height_n:
                continue

            if land[next_y][next_x] == 0:
                continue
            
            if visited[next_y][next_x] == 1:
                continue
                
            if land[next_y][next_x] == 1:
                land[next_y][next_x] = land[y][x] + 1
                visited[y][x] = 1
                queue.append((next_y, next_x))
                continue
    
    
    return petro_amount, cluster_map
    
def solution(land):
    
    land_width_m = len(land[0])
    land_height_n = len(land)
    
    clusters = {}
    
    cluster_map = [[0]*land_width_m for _ in range(land_height_n)]
    
    visited = [[0]*land_width_m for _ in range(land_height_n)]
    
    cluster_idx = 0
    max_petro_amount = 0
    
    for land_block_x in range(land_width_m):
        
        visited_cluster = set()
        
        for land_block_y in range(land_height_n):
            
             # 해당 블록과 겹치는 석유 덩어리 인덱스가 있는 경우
            if cluster_map[land_block_y][land_block_x]:
                visited_cluster.add(cluster_map[land_block_y][land_block_x])
                continue

            # 해당 블록과 겹치는 석유 덩어리가 없는 경우
            if land[land_block_y][land_block_x]:
                
                cluster_idx += 1
                visited_cluster.add(cluster_idx)
                
                # bfs를 통해서 새로운 석유 덩어리를 구함
                petro_amount, cluster_map = bfs([land_block_y, land_block_x], land, (land_width_m, land_height_n), visited, cluster_map, cluster_idx)
                
                clusters[cluster_idx] = petro_amount

        
        petro_amount = 0
        
        for idx in list(visited_cluster):
            petro_amount += clusters[idx]
        
        if petro_amount > max_petro_amount:
            max_petro_amount = petro_amount
            
    answer = max_petro_amount
    
    return answer