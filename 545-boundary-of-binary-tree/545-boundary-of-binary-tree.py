# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_leaf(self,root):
        '''
        Checks if the node is a leaf 
        '''
        if not root.left and not root.right:
            return True
        return False
    
    def left_boundary(self,root):
        '''
        Compute left boundary and return it as a list
        '''
        cur = root.left
        res = []
        while cur: 
            if self.is_leaf(cur) is False:
                res.append(cur.val)
            if cur.left is not None: 
                cur = cur.left
            else:
                cur = cur.right
        return res
    
    def right_boundary(self,root):
        '''
        Compute right boundary and return reverse of its list
        '''
        cur = root.right
        res = []
        while cur: 
            if self.is_leaf(cur) is False:
                res.append(cur.val)
            if cur.right is not None:
                cur = cur.right
            else: 
                cur = cur.left
        return res[::-1]
    
    def leaves(self,root):
        '''
        Compute all leaves from left to right
        '''
        if self.is_leaf(root):
            self.leaves_res.append(root.val)
            return 
        if root.left: self.leaves(root.left)
        if root.right: self.leaves(root.right)
        
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.leaves_res = []
        self.leaves(root)
        if self.is_leaf(root) is False:
            return [root.val,*self.left_boundary(root),*self.leaves_res,*self.right_boundary(root)]
        else: 
            return [root.val]