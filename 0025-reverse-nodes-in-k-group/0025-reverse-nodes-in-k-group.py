# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 1
        Idea:
        1. Use slow/fast pointer k steps apart
        2. Reverse between the slow and fast pointer everytime
            there is space to do so
        3. Use dummy node so that
            Slow pointer is always BEFORE the reverse list
            Fast pointer is always at the end (new head) of reverse
                list
        Complexity:
        - Time: O(2n) -> O(n)
            - One for iterate with fast ptr
            - One for reversing
        - Space: O(1)
    '''
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev = end.next
            while start != end:
                next = start.next
                start.next = prev
                prev = start
                start = next
            
            end.next = prev
            return end
                
        dummy_head = ListNode(next=head)
        slow = fast = dummy_head
        
        while True:
            for i in range(k):
                if not fast.next: return dummy_head.next
                fast = fast.next
            
            new_start = slow.next
            slow.next = reverse(slow.next, fast)
            slow = fast = new_start
        
        raise Exception('Execution should never reach this exp')