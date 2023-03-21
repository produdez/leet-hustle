# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 3
        Idea:
            Merkle hash
            Every node saves the hash of their child and we just compare the hash
        Complexity:
        - Time: O(m + n)
        - Space: O(log(n) + log(m) + m + n) 
            cause every node stores hash -> m+n
            cause we recursive both trees -> log(..) worse case (n+m)
            -> Total O(m+n) (worse than other approach but much faster)
    '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:       
        def merkle(root):
            if not root: return '#'
            root.merkle = str(hash(merkle(root.left) + str(root.val) + merkle(root.right)))
            return root.merkle
        
        merkle(root)
        merkle(subRoot)
        
        def dfs(root):
            if not root: return False
            
            return root.merkle == subRoot.merkle or dfs(root.left) or dfs(root.right)
        
        return dfs(root)