class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals.sort() # default list is sort by first value
        
        prev_end = intervals[0][1] # we only need the end to check overlap
        for start, end in intervals[1:]:
            if prev_end <= start: # cause sorted so it's ensure that prev cannot end before cur
                prev_end = end
            else:
                prev_end = min(prev_end, end)
                removed += 1
        return removed