# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        mapping = collections.defaultdict(list)
        x_min, x_max = 0,0
        queue = [(root,0)]
        while queue: 
            tmp = collections.defaultdict(list)
            for _ in range(len(queue)):
                node, x = queue.pop(0)
                tmp[x].append(node.val)
                
                if node.left: 
                    queue.append((node.left,x-1))
                    x_min = min(x_min,x-1)
                
                if node.right: 
                    queue.append((node.right,x+1))
                    x_max = max(x_max,x+1)
            
            for i in tmp:
                mapping[i] += tmp[i]
        return [mapping[i] for i in range(x_min,x_max+1)]