# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 2.5
            No extra space but same speed
        Idea:
            Merge first half with reversed second half
            Find half by using slow-fast pointer technique
            Use a dummy trick to make sure second > first 
                and avoid some complexity
        Complexity:
        - Time: O(n)
            -> Find half: n/2
            -> Reverse second: n/2
            -> Merge: n
            -> O(2n) total
        - Space: O(1)
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        # edge cases
        if not head or not head.next: return head
        
        # find half
        # add 1 to make sure second > first
        dummy = ListNode(next=head) 
        slow = fast = dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None # cut list
        
        # reverse second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev
        
        # merge
        dummy = curr = ListNode()
        first = head
        while first:
            curr.next = first
            first = first.next
            curr.next.next = second
            second = second.next

            curr = curr.next.next
        
        head = dummy.next
        
        