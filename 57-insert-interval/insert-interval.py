class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            
            # if interval is to the left of newInterval
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0] or newInterval[1] >= interval[0]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        res.append(newInterval)
        return res
            


        