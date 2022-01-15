# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if root is None: return []
            if root.val is None: return []
            queue = [root]
            final_result = []
            count = 0 
            while len(queue)>0:
                count += 1
                result = []
                for i in range(len(queue)):
                    current = queue.pop(0)
                    result.append(current.val)
                    if current.left is not None: queue.append(current.left)
                    if current.right is not None: queue.append(current.right)
                    
                    
                if count%2!=0:     
                    final_result.append(result)  
                else:
                    final_result.append(result[::-1])
            return final_result
        
        out = bfs(root)
        return out