class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque

        root = 0
        queue = deque([(graph[root], "0")])

        paths = []
        while queue:
            curr_node, path = queue.popleft()

            for next_idx in curr_node:
                new_path = path + ',' + str(next_idx)

                next_node = graph[next_idx]
                
                if not next_node and int(new_path.split(',')[-1]) == len(graph)-1:
                    
                    paths.append([int(s) for s in new_path.split(',')])
                    continue

                if int(new_path.split(',')[-1]) == len(graph)-1:
                    paths.append([int(s) for s in new_path.split(',')])

                queue.append([next_node, new_path])
        

        return paths



