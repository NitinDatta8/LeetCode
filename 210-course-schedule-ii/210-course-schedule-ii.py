'''
1. put into adjacency list 
2. run dfs on every course 
3. DFS()
    4. check if crs in cycle: return False 
    5. cehck if crs in visit: return True 
    add to cycle 
    run dfs on prereqs
    if dfs(pre) == False: return False 
    
    remove crs from cycle because there isnt one 
    add crs to visit 
    add crs to output
    return true
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites: 
            graph[crs].append(pre)
        
        output = []
        cycle, visit = set(), set()
        def dfs(crs): 
            if crs in visit: 
                return True
            if crs in cycle: 
                return False 
            
            cycle.add(crs)
            for pre in graph[crs]:
                if dfs(pre) == False:
                    return False 
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
                
        for crs in range(numCourses):
            if dfs(crs) == False: 
                return []
        
        return output