# Create a adjacency list 
# iterate over each element of adjacency list and do a dfs/bfs and mark visited nodes 
# once dfs/bfs is completed increment count by 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node1, node2 in edges: 
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = set()
        count = 0
        def bfs(node):
            queue = [node]
            for n in queue: 
                for nei in graph[n]: 
                    if nei not in visited: 
                        visited.add(nei)
                        queue.append(nei)
        
        
        for i in range(n):
            if i not in visited: 
                bfs(i)
                count += 1
        return count