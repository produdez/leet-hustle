# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version 1:
            Recursion?? non-optimal (i think)
        Idea:
            Move until have an equal node and check if the sub-tree from that node 
            is equal
        Complexity: 
        - Time: O(nm)?
        - Space: O(log(n)log(m))??
    '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p,q): 
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        if not root: return False
        
        return (sameTree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))