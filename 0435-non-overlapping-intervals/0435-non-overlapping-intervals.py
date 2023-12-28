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
        
        def pick_shortest(i1, i2):
            return i1 if i1[1] < i2[1] else i2
        
        prev = None
        for interval in intervals:
            # print(i)
            if prev is None: 
                prev = interval
            elif overlap(interval, prev): 
                # print('overlap: ', prev, interval)
                prev = pick_shortest(prev, interval)
                # print('shortest: ', prev)
                removed += 1
            else:
                prev = interval
        return removed