# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 1
        Idea:
            1. Use a double-headed queue
                And keep popping from left, right
                Constructing our result
            2. Start with a dummy node to remove
                edge cases
        Complexity:
        - Time: O(2n)
            -> Create queue n
            -> Pop n
        - Space: O(n)
            -> Queue contains ref to our list
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = collections.deque([])
        curr = head
        while curr:
            queue.append(curr)
            curr = curr.next
        
        dummy = ListNode()
        curr = dummy
        while True:
            if not queue: break
            else:
                curr.next = queue.popleft()
                curr = curr.next
            if not queue: break
            else:
                curr.next = queue.pop()
                curr = curr.next
        curr.next = None
        head = dummy.next