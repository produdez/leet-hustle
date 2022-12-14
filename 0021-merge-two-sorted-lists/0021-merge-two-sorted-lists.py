# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        

        if list1.val < list2.val:
            merged_head = list1
            list1 = list1.next
        else:
            merged_head = list2
            list2 = list2.next

        iter_merge = merged_head
        while True:
            if not list1:
                iter_merge.next = list2
                return merged_head
            if not list2:
                iter_merge.next = list1
                return merged_head
            

            if list1.val < list2.val:
                iter_merge.next = list1
                list1 = list1.next
            else:
                iter_merge.next = list2
                list2 = list2.next
            iter_merge = iter_merge.next
            
            