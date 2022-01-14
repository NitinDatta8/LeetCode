# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None: return 0 
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if abs(left_height-right_height)>1 or left_height ==-1 or right_height ==-1:
            return -1
        return max(left_height,right_height)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)!=-1
        