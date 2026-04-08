# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(curr):
            if not curr:
                return 0
            l=dfs(curr.left)
            r=dfs(curr.right)
            if l==-1:
                return -1
            if r==-1:
                return -1
            if abs(l-r)>1:
                return -1
            return 1+max(l,r)
        if dfs(root)!=-1:
            return True
        else:
            return False