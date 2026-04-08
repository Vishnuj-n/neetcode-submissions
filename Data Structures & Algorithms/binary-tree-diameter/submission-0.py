class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(curr):
            if not curr:
                return 0
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            
            # Update the global diameter
            # Diameter is the sum of left and right heights
            self.res = max(self.res, l + r)
            
            # RETURN: Max height of the subtree + 1 (the current node)
            return 1 + max(l, r) 
            
        dfs(root)
        return self.res