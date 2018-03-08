# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
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

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if len(left) + len(right) != len(intervals) :
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[-1 - len(right)].end)
        return left + [Interval(s, e)] + right
