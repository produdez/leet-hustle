# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 1
            DFS stack
    '''
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxVal):
            if not root: return 0
            
            newMax = max(maxVal, root.val)
            leftGood = dfs(root.left, newMax)
            rightGood = dfs(root.right, newMax)
            
            return leftGood + rightGood + (1 if newMax == root.val else 0)
        
        return dfs(root, root.val)