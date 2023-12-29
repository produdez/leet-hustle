class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals.sort(key=lambda i: i[0])
        
        prev = None
        for interval in intervals:
            if prev is None or prev[1] <= interval[0] or interval[1] <= interval[0]: 
                prev = interval
            else:
                prev = prev if prev[1] < interval[1] else interval
                removed += 1
        return removed