class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        
        for i in range(1, len(intervals)):
            first, second = intervals[i - 1], intervals[i]
            if first[1] > second[0]:
                return False
        
        return True


        