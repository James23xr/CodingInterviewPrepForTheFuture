"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        all_intervals = []
        for employee in schedule:
            for interval in employee:
                all_intervals.append(interval)
        all_intervals.sort(key=lambda x:x.start)
        result = []
        busy_until = all_intervals[0].end
        for interval in all_intervals[1:]:
            if interval.start > busy_until:
                result.append(Interval(busy_until,interval.start))
            busy_until = max(busy_until,interval.end)
        return result

        