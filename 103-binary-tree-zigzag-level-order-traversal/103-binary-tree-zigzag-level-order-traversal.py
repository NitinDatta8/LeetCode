class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = [root]
        my_res = []
        count = 0 
        while queue: 
            res = []
            count += 1
            for i in range(len(queue)):
                cur = queue.pop(0)
                res.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            if count % 2 != 0: 
                my_res.append(res)
            else: 
                my_res.append(res[::-1])
        return my_res