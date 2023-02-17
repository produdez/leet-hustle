# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 2.9
            No extra space but same speed
            Update: No shitty dummy tricks
                and use a different merge tech
        Idea:
            Merge first half with reversed second half
            Find half by using slow-fast pointer technique
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
        slow, fast = head, head.next
        while fast and fast.next:
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
        first = head
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
        
        
        