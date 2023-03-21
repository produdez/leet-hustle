# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
        Version: 1
            Recursive
        Idea:
            Since BST, a node that's between p <= node <= q 
            is the LCA
            Cause if you move right, you loose the smaller node as a child
            and if move left, loose the larger node as a child
        Complexity:
        - Time: O(d)
        - Space: O(d) call stack
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root