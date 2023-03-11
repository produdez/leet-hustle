# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Version 3.5:
            Refac code
            Morris traversal
            -> No stack / No Recursion
        Idea:
            Add additional pointer to guide our traversal
            - DFS -> We're traveling all left then right 
            - And swapping (inversing) on every node we visit
            - * Main idea: Every time we attempt to traverse to next node (left)
                We need to make sure the last node visited on the sub-tree that we travel
                have a pointer back to the current node
                -> Meaning we set a path from last visited to current
            - When hit deadend -> We go back to parent and traverse the right branch (cause dfs)
            - If there's no right branch on any parent -> End cause the treee is left lopsided
            - If there's no parent -> We have ended on the last node on the right of the tree
                -> END
                
            * NOTE *
            - Since we're swapping at every node 
            -> The last node we visit turns out to be the left-most child
            -> Why?
                1. Since we inverse the tree and do dfs, last node should be the 
                    inverse of the predecesor node
                    * pred node is right most on left branch
                    -> inverse -> left most on right branch
                2. BUT * big but since we only inverse one level at a time
                    -> the node we're looking for at the time that level is inversed
                    -> will be left most on left branch -> left most node!
        Complexity:
        - Time: O(2n) (Extra time to find decendant) -> O(n)
        - Space: Extra space on the tree itself
            * If parent path is deleted after use -> O(logN) or O(d)
            * else it's just O(n)
            
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def descendant(root): 
            # the code make sure root here always have left
            while root.left: root = root.left
            return root

        curr = root
        while curr:
            # swap
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                # set link from last decendant to parent
                descendant(curr).parent = curr
                curr = curr.left
            elif curr.right:
                curr = curr.right
            else:
                right_branch = None
                while hasattr(curr, 'parent'):
                    parent = curr.parent
                    delattr(curr, 'parent') # delete link
                    curr = parent
                    if curr.right: 
                        right_branch = curr.right
                        break

                curr = right_branch
        
        return root

        