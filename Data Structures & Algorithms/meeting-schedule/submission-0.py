"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #essentially we care if end bigger than next start
        #we go through, take the max, and compare the next start 

        intervals.sort(key=lambda x: x.start)

        max_end = 0 #must be pos  

        for interval in intervals:
            if interval.start < max_end: #same time is ok
                return False

            max_end = interval.end
            
        return True  

        