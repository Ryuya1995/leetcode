# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        i = 1
        intervals = sorted(intervals, key=lambda x: x.start)
        while i < len(intervals):
            if intervals[i].start <= intervals[i - 1].end:
                if intervals[i].end >= intervals[i - 1].end:
                    intervals[i - 1].end = intervals[i].end
                del intervals[i]
            else:
                i += 1
        return intervals
