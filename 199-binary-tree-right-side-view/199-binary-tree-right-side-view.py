# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        mapping = []
        queue = [root]
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
                    
            mapping.append(tmp)
        return [i[0] for i in mapping]