# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
        Version: 2
            Iterative
        Idea:
            Since BST, a node that's between p <= node <= q 
            is the LCA
            Cause if you move right, you loose the smaller node as a child
            and if move left, loose the larger node as a child
        Complexity:
        - Time: O(d)
        - Space: O(1)
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val > p.val and root.val > q.val: root = root.left
            elif root.val < p.val and root.val < q.val: root = root.right
            else:
                return root

        raise Exception('This function should not reach this part')