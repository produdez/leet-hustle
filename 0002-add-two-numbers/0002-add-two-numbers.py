# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 1.5
            Same but single loop, maybe less efficient
        Idea:
            Basic summary with remainder carry through
        Complexity:
        - Time: O(n)
        - Space: O(1)
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        remainder = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + remainder
            
            curr.next = ListNode(val%10)
            remainder = val // 10

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if remainder: curr.next = ListNode(remainder)
        return dummy.next