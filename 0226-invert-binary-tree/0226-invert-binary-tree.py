# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 1
        Idea:
            Invert all child and swap
            Note that no need to check for leaf
            The only edge case is if none return none
        Complexity:
        - Time: O(n)
        - Space: O(log(n)) for the call stack
            Cause it calls down depth first 
            -> stack is equal to depth of tree
            -> log2(n)
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root