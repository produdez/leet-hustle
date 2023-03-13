# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def left_most(root):
            temp = root
            while temp.left and temp.left != root: temp = temp.left
            return temp
        
        def descendant(root):
            root = root.left
            while root.right: root = root.right
            return root

        curr = root
        while curr:
            if not curr.left:
                curr.left, curr.right = curr.right, curr.left
                curr = curr.left
            else:
                last_left = left_most(curr)
                if not last_left.left: # no cycle
                    descendant(curr).right = curr
                    curr = curr.left
                else: 
                    # means there's a cycle back to root
                    if last_left: last_left.left = None
                    curr.left, curr.right = curr.right, curr.left # swap
                    curr = curr.left
        return root