# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 1
        Idea: Two pointer
        1. One points to current node, initially head
            -> when moved all, this becomes null
        2. One points to previous, initially null
            -> when moved all, this becomes the last node,
            Meaning the new reversed head
        3. Repeat:
            - save current node.next (since link will be lost)
            - curr node.next = prev (reverse)
            - move previous: previous = curr
            - move curr: curr = saved next
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revHead = None
        while head:
            nxt = head.next
            head.next = revHead
            
            revHead = head
            head = nxt
        return revHead
        