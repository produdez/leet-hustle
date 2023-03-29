# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        
        queue = collections.deque([[root]])
        result = []
        while queue:
            current_level = []
            next_level = []
            for node in queue.popleft():
                current_level.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            
            result.append(current_level)
            if next_level: queue.append(next_level)
            
        return result
            