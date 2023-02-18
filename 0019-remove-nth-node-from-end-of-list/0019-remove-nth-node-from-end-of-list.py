# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 1
        Idea:
        1. Use two pointer n-nodes appart to find target node
        2. Use prev pointer to bridge the gap
        Complexity:
        - Time: O(n)
        - Space: O(1)
    '''
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