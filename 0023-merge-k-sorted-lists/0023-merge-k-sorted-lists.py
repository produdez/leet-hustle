# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Version: 2
        Idea: Divide and Conquer
        - Merge Two list at a time
            Ex: 4 list size X -> 2 list size 2x 
                -> 1 list size 4x
        Complexity:
        - Time: O(n.log(k))
            1. Since k lists and we're merging half each
                -> Log(k) merges
            2. Algorithm runs through every node twice
                -> 2n (2 cause once in child merges and
                    another time at the last merge)
            3. -> Total O(nlogk)
        - Space: O(logk) cause have to store result
            of sub-problems
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = curr = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next
        
        merged = lists
        while len(merged) > 1:
            new_merged = []
            for i in range(0, len(merged), 2):
                if i + 1 < len(merged):
                    new_merged.append(merge(merged[i], merged[i+1]))
                else:
                    new_merged.append(merged[i])
            merged = new_merged
        
        return merged[0] if merged else None
        
        
        