# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        if root.val is None: return 
        queue = [root]
        res = []
        while len(queue)>0:
            size = len(queue)
            my_res = []
            for i in range(size):
                cur = queue.pop(0)
                if cur.left is not None: queue.append(cur.left)
                if cur.right is not None: queue.append(cur.right)
                my_res.append(cur.val)
            res.append(my_res)
        return res