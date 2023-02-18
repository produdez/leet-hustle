# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        for _ in range(n):
            end = end.next
        
        dummy = prev = ListNode(next=head)
        target = head
        while end:
            prev = target
            end = end.next
            target = target.next
        
        prev.next = target.next
        return dummy.next