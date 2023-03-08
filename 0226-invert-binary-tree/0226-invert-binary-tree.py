# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 2
            Non recursive with stack
        Idea: DFS with stack
        Compleixty: Same
        - Time: O(n)
        - Space: O(log(n)) = O(d)
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr: continue
            curr.left, curr.right = curr.right, curr.left
            stack.append(curr.right)
            stack.append(curr.left)
        
        return root