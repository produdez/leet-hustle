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
        Version: 1.5
            Update a better single loop
        Idea:
        1. Use HashMap to save link between old node and 
            new duplicated node
        2. Iterate and
            if link exist -> means created -> just link
            else create and then link and add to link HashMap
            do the same for node.random
        Complextity:
        - Time: O(n)
        - Space: O(n)
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        link = collections.defaultdict(lambda: None)
        
        new = Node(0)
        new_node = new
        while head:
            # link
            if not link[id(head)]:
                # create
                new_node.next = Node(head.val)
                link[id(head)] = new_node.next
            else:
                new_node.next = link[id(head)]

            new_node = new_node.next
            
            # link/create random also
            if head.random is not None:
                if not link[id(head.random)]:
                    new_node.random = Node(head.random.val)
                    link[id(head.random)] = new_node.random
                else:
                    new_node.random = link[id(head.random)]
            
            # shift
            head = head.next
        
        return new.next