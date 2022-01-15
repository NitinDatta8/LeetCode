# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        mapping = []
        queue = [root]
        while queue: 
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            mapping.append(tmp)
        return mapping[-1][0]