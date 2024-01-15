# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfsSum(node: Optional[TreeNode]) -> (int, int):
            if not node: return -math.inf, -math.inf
            
            val = node.val
            leftMaxPath, leftMaxBranch = dfsSum(node.left)
            rightMaxPath, rightMaxBranch = dfsSum(node.right)
            
            maxBranch = max(val, val + leftMaxBranch, val + rightMaxBranch)
            maxPath = max(
                maxBranch, leftMaxPath, rightMaxPath,
                val + leftMaxBranch + rightMaxBranch
            )
            
            return maxPath, maxBranch
        
        
        maxPath, _ = dfsSum(root)
        return maxPath