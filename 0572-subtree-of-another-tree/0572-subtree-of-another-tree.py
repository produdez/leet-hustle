# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version 2:
            Stack naive dfs approach
        Idea:
            check match at each step while dfs-sing
        Complexity:
        - Time: O(mn)
        - Space: O(logmlogn)
    '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        stack = [root]
        
        def isSame(p,q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        while stack:
            node = stack.pop()
            if node.val == subRoot.val and isSame(node, subRoot):
                return True
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return False