'''
create an adjacency list to store course as key and its prereqs as values (in a list)
visit, cycle empty sets

DFS(course)
to check base condition check if course in cycle return false and if it is in visit return true 
add current course to cycle 
run dfs on its prereqs and if dfs(prereq) is False return False 
remove from cycle 
add in visit
add to ouput 
return true 

iterate over all courses and do dfs 
if anyone return false return []
return output at end 
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites: 
            graph[crs].append(pre)
        
        output = []
        cycle, visit = set(), set()
        def dfs(crs): 
            if crs in cycle: 
                return False 
            if crs in visit: 
                return True 
            
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