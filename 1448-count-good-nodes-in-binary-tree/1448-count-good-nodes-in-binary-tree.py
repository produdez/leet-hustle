# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 1
            DFS stack
    '''
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        stack = [(root, root.val)]
        count = 0
        while stack:
            cur, cur_max = stack.pop()
            if cur.val >= cur_max: count += 1
                
            if cur.left: stack.append((cur.left, max(cur_max, cur.left.val)))
            if cur.right: stack.append((cur.right, max(cur_max, cur.right.val)))
        return count