# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 1
        Idea: Recursion
        Complexity: 
        - Time: O(n)
        - Space: O(d)
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )
        