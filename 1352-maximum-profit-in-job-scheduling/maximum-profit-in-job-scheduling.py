class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        dp = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            
            if i in dp:
                return dp[i]
            
            # skip curr
            res = dfs(i + 1)

            # take curr
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            dp[i] = res = max(res, intervals[i][2] + dfs(j))
            return res
        
        return dfs(0)
        