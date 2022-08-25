# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None: 
            return True
        if root is None: 
            return False 
        
        if self.sametree(root, subRoot): 
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sametree(self, p, q): 
        if not p and not q: 
            return True
        
        if p and q and p.val == q.val: 
            return self.sametree(p.left, q.left) and self.sametree(p.right, q.right)