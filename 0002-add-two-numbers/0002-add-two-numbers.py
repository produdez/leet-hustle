# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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
        
        remaining_list = l1 if l1 else l2
        while remaining_list:
            val = remaining_list.val + remain
            cur.next = ListNode(val % 10)
            remain = val // 10
            remaining_list = remaining_list.next
            cur = cur.next
        if remain: cur.next = ListNode(remain)

        return dummy.next