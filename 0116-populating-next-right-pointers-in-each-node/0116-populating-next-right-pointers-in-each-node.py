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
            Version 21: best solution, cleaner code
            Idea:
            
            Similar to a naive BFS solution where you use a queue to traverse 
            and link nodes from same level

            Here since we have "right" pointer, we use a current and next pointer
            and that "right-ness" to simulate a queue (aka BFS) without ever creating one

        '''
        
        
        curr, nxt = root, root.left if root else None
        while curr and nxt:
            # connect left and right of node
            curr.left.next = curr.right
            
            # connect right to the neighboring tree if any
            if curr.next:
                curr.right.next = curr.next.left
            
            #shift
            curr = curr.next # continue same level
            if not curr: # switching level
                curr = nxt
                nxt = nxt.left
            
        return root