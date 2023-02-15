# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version 2:
            Different implementation
        Idea: Recursive
            Construct the reversedHead recursively revHead and head
            - revHead starts as None (empty reversed list)
            - head is head
            And we keep expanding revHead with the current head
            till our head is empty -> our revHead is done
        Complexity:
        - Time: O(n)
        - Space: O(1)
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(rHead, head):
            if not head: return rHead
            
            nxt = head.next
            head.next = rHead
            return recursive(head, nxt)
        
        return recursive(None, head)