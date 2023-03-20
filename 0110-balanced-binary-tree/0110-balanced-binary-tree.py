# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 1.5
            Add early stop 
        Idea: 
            Recursive post-order + global var to keep track of balance-ness of all nodes
        Complexity:
        - Time: O(n)
        - Space: O(d) - worse O(n)
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def depth(root):
            if not root or not balanced[0]: return -1
            leftHeight = depth(root.left)
            rightHeight = depth(root.right)
            
            if abs(leftHeight - rightHeight) > 1: 
                balanced[0] = False
            return 1 + max(leftHeight, rightHeight)
        
        depth(root)
        return balanced[0]