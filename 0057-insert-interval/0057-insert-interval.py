class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0 
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            i += 1

        start = i
        while i < len(intervals) and newInterval[1] >= intervals[i][0]: # overlap
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # instead of deleting each, which will make our time complexity O(n^2)
        # we use slicing deletion to delete a range of element which only takes O(n + k) ~ O(n)
        # with k being slice size
        del intervals[start:i] 
        intervals.insert(start, newInterval)
        return intervals


        
