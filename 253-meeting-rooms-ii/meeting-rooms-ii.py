class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i for i, j in intervals])
        ends = sorted([j for i, j in intervals])

        roomsUsed, maxRoomsUsed = 0, 0

        s, e = 0, 0

        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                roomsUsed += 1
            else:
                e += 1
                roomsUsed -= 1
            
            maxRoomsUsed = max(maxRoomsUsed, roomsUsed)
        
        return maxRoomsUsed