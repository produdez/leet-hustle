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
            # print(f'at: {curr.val}')
            cycle = left_most(curr)
            # print(f'left_most of {curr.val} is {cycle.val if cycle else None}')
            if not cycle or cycle.left == curr: # means have cycle
                # swap
                if cycle: cycle.left = None
                # print(f'swapping at: {curr.val}')
                curr.left, curr.right = curr.right, curr.left
                curr = curr.left
            else:
                # link
                des = descendant(curr)
                des.right = curr
                # print(f'descendant of {curr.val} is {des.val}')
                curr = curr.left
        return root