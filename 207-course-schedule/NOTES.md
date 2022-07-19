convert the prerequisites to adjacency list using hashmap
use for loop iterating and do dfs for each course
create a visited set
DFS()
if course in visted return False
if course doesnt have any prereq return True
add course to visited
traverse prereqs for current course and do dfs
if not dfs(pre) return False
​
remove course from visited
set prereqs for current course to empty
return True
​