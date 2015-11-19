# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x:x.start)
        room = []
        ans = 0
        for inte in intervals:
            ri = -1
            for i in range(ans):
                if room[i] <= inte.start:
                    ri = i
                    break
            if ri == -1:
                ri = ans
                ans += 1
                room.append(0)
            room[ri] = inte.end
        return ans