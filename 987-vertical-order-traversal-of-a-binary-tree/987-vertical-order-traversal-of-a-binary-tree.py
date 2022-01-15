class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """    
        mapping = collections.defaultdict(list) 
        queue = [(root,0)]
        x_min, x_max = 0, 0
        while queue:
            tmp = collections.defaultdict(list)
            for _ in range(len(queue)):
                node, x = queue.pop(0)
                tmp[x].append(node.val) 
                
                if node.left:
                    queue.append((node.left, x-1))
                    x_min = min(x_min, x-1)
                if node.right: 
                    queue.append((node.right, x+1)) 
                    x_max = max(x_max, x+1)
            for i in tmp: 
                mapping[i] += sorted(tmp[i])
        return [mapping[i] for i in range(x_min, x_max+1)]
