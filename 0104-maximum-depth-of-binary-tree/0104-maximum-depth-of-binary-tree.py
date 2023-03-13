# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 3
        Idea: BFS
        Complexity: 
        - Time: O(n)
        - Space: O(d)
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            # iterate all nodes in same level
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return level
            
            
            
        