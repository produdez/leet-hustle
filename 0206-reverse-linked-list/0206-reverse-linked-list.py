# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 2.5
            Advanced recursive
        Idea:
            Imagine our list 1 -> 2 -> 3  
            If we reverse after 1 
            we have: 1 -> 2 <- 3 (2 points to None also)
            That's the idea:
            1. We reverse after current node
            2. Current node always points to tail of reverse list
                so we use that curr.next.next to point reverse tail
                to current node
            3. Always set the current node.next to None
                to make sure the reversed list is terminated and no
                loop
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        revHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return revHead