# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 1
        Idea:
        1. Merge using digit sum + remainder carry through
        2. Merge until one list runs out and continue with leftover
        3. Use dummy to remove complication
        4. Make sure to add one more carry through if remainder is
            not 0 at the end
        Complexity:
        - Time: O(max(m,n))
        - Space: O(1)
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        remain = 0

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            val = val1 + val2 + remain

            cur.next = ListNode(val % 10)
            remain = val // 10

            cur = cur.next            
            l1 = l1.next
            l2 = l2.next
        
        leftover = l1 if l1 else l2
        while leftover:
            val = leftover.val + remain
            cur.next = ListNode(val % 10)
            remain = val // 10

            leftover = leftover.next
            cur = cur.next
        
        if remain > 0: cur.next = ListNode(remain)
        return dummy.next