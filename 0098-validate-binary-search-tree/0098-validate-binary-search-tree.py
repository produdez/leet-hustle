# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 1
            DFS
        
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_validate(root, min=None, max=None):
            if not root: return True
            if min is not None and root.val <= min: return False
            if max is not None and root.val >= max: return False
            
            return  dfs_validate(root.left, min, root.val) and \
                    dfs_validate(root.right, root.val, max)
        
        return dfs_validate(root)
                