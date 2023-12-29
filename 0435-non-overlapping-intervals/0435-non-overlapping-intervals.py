class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals.sort(key=lambda interval: interval[0])
        # print('-----start-----')
        # print(list(enumerate(intervals)))
        def overlap(i1, i2):
            if i2[0] < i1[1] <= i2[1] or i1[0] < i2[1] <= i1[1]:
                return True
            return False
        
            
        prev = None
        for interval in intervals:
            # print(i)
            if prev is None or prev[1] <= interval[0] or interval[1] <= interval[0]: 
                prev = interval
                continue
                # print('overlap: ', prev, interval)
            prev = prev if prev[1] < interval[1] else interval
            # print('shortest: ', prev)
            removed += 1
        return removed