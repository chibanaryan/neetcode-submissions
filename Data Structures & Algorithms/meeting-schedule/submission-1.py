"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:(x.start, x.end))
        if len(intervals) <= 1:
            return True
        most_recent_end = intervals[0].end
        for i in intervals[1:]:
            if i.start < most_recent_end:
                return False
            most_recent_end = i.end
        return True