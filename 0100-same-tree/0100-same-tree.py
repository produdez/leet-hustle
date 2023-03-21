# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 1
            Recursive
        Idea:
            DFS: compare current and then left, right
            Note that 3 cases 
            - None / None
            - None / Something
            - Something / Something
        Complexity:
        - Time: O(n)
        - Space: O(d) depth, worse case O(n)
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        