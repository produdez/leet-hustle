"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    '''
        Version: 1.9
            Same idea, cleanest code, maybe bit less
        Idea:
            Two passes - Two loop
            One to just clone and link old to new nodes
            Another to link all the next, random pointer
        Complexity:
        - O(n) both
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        link = {None: None}
        
        curr = head
        while curr:
            link[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            link[curr].next = link[curr.next]
            link[curr].random = link[curr.random]
            curr = curr.next

        return link[head]