"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_new = {}
        
        def dfs(node):
            if node in old_new: 
                return old_new[node]
            
            copy = Node(node.val)
            old_new[node] = copy
            for nei in node.neighbors: 
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None