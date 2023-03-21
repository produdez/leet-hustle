# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        
        while stack:
            a,b = stack.pop()
            
            if not a and not b: 
                continue
            elif a and b and a.val == b.val:
                stack.append((a.right, b.right))
                stack.append((a.left, b.left))
            else:
                return False
        return True