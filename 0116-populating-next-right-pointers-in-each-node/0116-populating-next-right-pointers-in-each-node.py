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
            Version 1.1: interative, same idea, just not recursion
            Idea:
            At every node, you have two pointers
                1. A go right pointer on your left child (always move right)
                2. A go left pointer on your right child (always move left)
            These two pointer will ilterate together and connect:
                - Left child and right child of current node
                - All the outer right-most node of the left tree with all the outer left-most node of the right tree
        '''
        if not root: return root        
        queue = [root]
        while queue:
            curr = queue.pop()
            left = curr.left
            right = curr.right
        
            while left and right:
                left.next = right
                left = left.right
                right = right.left

            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)

        return root