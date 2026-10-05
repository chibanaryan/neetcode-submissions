"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        room_end_times = []
        for i in intervals:
            if room_end_times and room_end_times[0] <= i.start:
                heapq.heappop(room_end_times)
            heapq.heappush(room_end_times, i.end)
        return len(room_end_times)