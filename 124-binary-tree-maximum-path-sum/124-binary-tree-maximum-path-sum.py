# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        def maxp(node):
            if node is None: return 0

            left_sum = max(maxp(node.left),0)
            right_sum = max(maxp(node.right),0)
            self.maxi = max(self.maxi,node.val+left_sum+right_sum)
            return node.val + max(left_sum, right_sum)
        
        val = maxp(root)
        return self.maxi