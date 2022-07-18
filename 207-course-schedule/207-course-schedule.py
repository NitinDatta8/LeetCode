class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        
        for pre, crs in prerequisites: 
            graph[crs].append(pre)
            
        visit = set()
        def dfs(crs):
            if crs in visit: 
                return False 
            if graph[crs] == []: 
                return True 
            
            visit.add(crs)
            for pre in graph[crs]:
                if not dfs(pre): 
                    return False 
            
            visit.remove(crs)
            graph[crs] = []
            return True 
        
        for crs in range(numCourses): 
            if not dfs(crs): 
                return False 
        
        return True