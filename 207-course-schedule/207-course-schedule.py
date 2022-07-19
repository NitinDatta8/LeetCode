'''
convert the prerequisites to adjacency list using hashmap 
use for loop iterating and do dfs for each course 
create a visited set
DFS()
if course in visted return False 
if course doesnt have any prereq return True 
add course to visited 
traverse prereqs for current course and do dfs
if not dfs(pre) return False 

remove course from visited 
set prereqs for current course to empty 
return True 

'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites: 
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