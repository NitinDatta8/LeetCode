class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dst: int) -> bool:
        graph = defaultdict(list)
        queue = deque()
        for node1, node2 in edges: 
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        queue.append(src)
        visited = set()
        while queue: 
            cur_node = queue.popleft()
            if cur_node == dst: 
                return True 
            visited.add(cur_node)
            for neighbor in graph[cur_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False