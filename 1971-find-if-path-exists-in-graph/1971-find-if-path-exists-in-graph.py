class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        
        def build_graph(edges):
            graph = {}
            for e in edges: 
                a, b = e
                if a not in graph: 
                    graph[a] = []
                if b not in graph: 
                    graph[b] = []
                
                graph[a].append(b)
                graph[b].append(a)
            
            return graph 
        
        def dfs(graph, src, dst, visited):
            if src == dst: 
                return True 
            if src in visited: 
                return False 
            
            visited.add(src)
            
            for neighbor in graph[src]:
                if dfs(graph, neighbor, dst, visited) == True: 
                    return True 
            
            return False 
        
        # Build the graph 
        graph = build_graph(edges)
        
        # Run DFS 
        return dfs(graph, source, destination, visited)