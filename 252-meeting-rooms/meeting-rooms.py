class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            one, two = intervals[i - 1], intervals[i]

            # second starts before 1st ends
            if two[0] < one[1]:
                return False
        return True


        