# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root: return 0
            return max(depth(root.left), depth(root.right)) + 1
        
        if not root: return 0
        l_depth = depth(root.left)
        r_depth = depth(root.right)
        if l_depth == r_depth:
            return l_depth + r_depth
        elif l_depth > r_depth:
            return max(
                self.diameterOfBinaryTree(root.left),
                l_depth + r_depth
            )
        else:
            return max(
                self.diameterOfBinaryTree(root.right),
                l_depth + r_depth
            )