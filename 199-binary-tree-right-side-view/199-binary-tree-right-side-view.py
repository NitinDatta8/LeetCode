class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        
        def dfs(root, depth):
            if root == None: return
            if depth == len(self.ans):  # When we meet this `depth` for the first time, let's add the first node as the right side most node.
                self.ans.append(root.val)
            dfs(root.right, depth + 1)  # Go right side first
            dfs(root.left, depth + 1)
            
        dfs(root, 0)
        return self.ans