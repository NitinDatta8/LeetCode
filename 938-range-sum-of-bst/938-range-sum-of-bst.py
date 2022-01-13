# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None: return 0 
        total = 0
        stack = [root]
        while len(stack)>0:
            cur = stack.pop()
            if low <= cur.val <= high: 
                total += cur.val 
            
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
        return total
            