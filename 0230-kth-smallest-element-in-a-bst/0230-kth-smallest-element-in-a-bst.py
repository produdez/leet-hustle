# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version 3:
            Improved recursion with early stop
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def find(node):
            nonlocal k
            nonlocal res
            
            if not node: return
            
            if node.left: find(node.left)
            
            k -= 1
            if k == 0: res = node.val
            if k <= 0: return
            
            find(node.right)
        
        find(root)
        return res