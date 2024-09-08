# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: return float('-inf'), float('-inf')

            lnorm, lsplit = dfs(root.left)
            rnorm, rsplit = dfs(root.right)

            norm = max(root.val, root.val + lnorm, root.val + rnorm)
            split = max(
                root.val + lnorm + rnorm,
                lsplit,
                rsplit,
                norm
            )

            return norm, split
        
        norm, split = dfs(root)
        return max(norm, split)