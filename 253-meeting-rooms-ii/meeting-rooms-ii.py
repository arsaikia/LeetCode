class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i for i, j in intervals])
        ends = sorted([j for i, j in intervals])

        count = 0
        maxCount = 0

        s, e = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            maxCount = max(maxCount, count)

        return maxCount
            

            