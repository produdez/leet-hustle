"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
            Version 2: best solution
            Idea:
            
            Similar to a naive BFS solution where you use a queue to traverse 
            and link nodes from same level

            Here since we have "right" pointer, we use a current and next pointer
            and that "right-ness" to simulate a queue (aka BFS) without ever creating one

        '''
        if not root: return root        
        
        top, level_head = root, root.left
        while level_head:
            level_head.next = top.right
            curr = top.right
            top = top.next
            
            while top:
                curr.next = top.left
                top.left.next = top.right
                curr = top.right
                top = top.next
            
            top = level_head
            level_head = level_head.left
        return root