# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version: 1
        Idea:
            In-order traverse one level at a time
        Complexity:
        - Time: O(n)
        - Space: O(last_level)
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        
        current_level = [root]
        result = []
        while current_level:
            next_level = []
            traverse = []
            for node in current_level:
                traverse.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            
            result.append(traverse)
            current_level = next_level
            
            
        return result
            