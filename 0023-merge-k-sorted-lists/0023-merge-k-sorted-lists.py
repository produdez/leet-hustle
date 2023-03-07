# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 1
        Idea:
        - Keep a priority queue of size K to keep the head of lists
            sorted.
        - Just keep poping min node from the queue and add to merged 
            list until empty
        Complexity:
        - Space: O(k) The queue is initialized as storing all heads of each list
            -> means max size is k -> O(k)
        - Time: O(2log(k) * n) with n being total number of elements
            -> Cause each element is added and popped from queue
            -> so N times 2 times log(k) -> O(n.log(k))
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        queue = []
        
        for idx, head in enumerate(lists):
            if not head: continue    
            heapq.heappush(queue, (head.val, idx, head))
            
        while queue:
            _, idx, head = heapq.heappop(queue)
            curr.next = head
            curr = curr.next
            if not queue: break
            if head.next: heapq.heappush(queue, (head.next.val, idx, head.next))
        
        return dummy.next
                