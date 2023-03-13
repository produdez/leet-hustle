# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 2
        Idea: Stack
        Complexity: 
        - Time: O(n)
        - Space: O(d)
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        maxDepth = 0
        while stack:
            curr, depth = stack.pop()
            if curr:
                stack.append((curr.left, depth + 1))
                stack.append((curr.right, depth + 1))
            else:
                # only update at leaf to save some ops
                maxDepth = max(depth, maxDepth)
        return maxDepth
            
            
            
        