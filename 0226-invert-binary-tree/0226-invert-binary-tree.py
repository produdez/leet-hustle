# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def left_most(root):
            temp = root.left
            if not temp: return None
            while temp.left and temp.left != root: temp = temp.left
            return temp
        
        def descendant(root):
            root = root.left
            while root.right: root = root.right
            return root

        curr = root
        while curr:
            last_left = left_most(curr)
            if not last_left or last_left.left == curr: 
                # remove link if there's a used cycle
                if last_left: last_left.left = None
                curr.left, curr.right = curr.right, curr.left # swap
                curr = curr.left
            else:
                descendant(curr).right = curr
                curr = curr.left
        return root