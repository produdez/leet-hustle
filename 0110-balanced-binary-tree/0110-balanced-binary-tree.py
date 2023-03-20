# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 2
        Idea: 
            Iterative post-order
        Complexity:
        - Time: O(n)
        - Space: O(d) - worse O(n)
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack = [root]
        depth = {None: -1}
        while stack:
            node = stack[-1]
            if node.left in depth and node.right in depth:
                stack.pop()
                if abs(depth[node.left] - depth[node.right]) > 1:
                    return False
                
                depth[node] = 1 + max(depth[node.left], depth[node.right])
                if node.left: del depth[node.left]
                if node.right: del depth[node.right]
            else:
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return True