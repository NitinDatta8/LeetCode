# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None: return []
        stack = [(root,"")]
        res = []
        while stack:
            node,ls = stack.pop()
            if node.left is None and node.right is None:
                res.append(ls + str(node.val))
            if node.left: 
                stack.append((node.left,ls+str(node.val)+'->'))
            if node.right:
                stack.append((node.right,ls+str(node.val)+'->'))
        return res 
