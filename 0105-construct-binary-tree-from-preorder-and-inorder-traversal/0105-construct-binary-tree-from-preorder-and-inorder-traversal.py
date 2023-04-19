# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version 1:
            The elegant/naive/very stupid recursion approach
        Complexity:
            Divide and conquer so O(nlogn)
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder[0])
        idx_root = inorder.index(root.val)
        if idx_root == 0: pass
        elif idx_root == 1: root.left = TreeNode(inorder[0])
        else: root.left = self.buildTree(preorder[1:idx_root + 1], inorder[:idx_root])
        root.right = self.buildTree(preorder[idx_root+1:], inorder[idx_root+1 :])
        return root