# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return []
        my_res = []
        queue = [root]
        while len(queue)>0:
            res = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur.left is not None: queue.append(cur.left)
                if cur.right is not None: queue.append(cur.right)
                res.append(cur.val)
            
            my_res.append(res)
        max_sum = float('-inf')
        max_index = 0 
        for i,j in enumerate(my_res): 
            # print(i,j)
            if sum(j) > max_sum: 
                max_sum = sum(j)
                max_index = i
        return max_index+1
            