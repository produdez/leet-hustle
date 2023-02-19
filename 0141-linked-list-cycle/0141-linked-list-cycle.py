# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
        Version: 1
        Idea:
            Use slow/fast pointer (turtle and hare)
                for cycle detection
        Complexity:
        - Time: ??
        - Space: O(1)
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow, fast = head, head.next
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast: return True
        return False