# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def depth(root):
            if not root: return -1
            leftHeight = depth(root.left)
            rightHeight = depth(root.right)
            
            if abs(leftHeight - rightHeight) > 1: 
                balanced[0] = False
            return 1 + max(leftHeight, rightHeight)
        
        depth(root)
        return balanced[0]