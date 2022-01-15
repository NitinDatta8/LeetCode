# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            node = queue.pop(0)
            res = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return res