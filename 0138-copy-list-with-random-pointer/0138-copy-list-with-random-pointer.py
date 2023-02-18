"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ref = {}
        
        newHead = Node(0)
        curOld = head
        curNew = newHead
        while curOld:
            curNew.next = Node(curOld.val)
            curNew = curNew.next
            
            ref[id(curOld)] = curNew
            curOld = curOld.next
        
        curNew = newHead.next
        curOld = head
        while curOld:
            if curOld.random: curNew.random = ref[id(curOld.random)]
            curOld = curOld.next
            curNew = curNew.next
        return newHead.next