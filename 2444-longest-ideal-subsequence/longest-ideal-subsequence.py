class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for c in s:
            key = ord(c) - ord("a")
            longest = 1
            for prev in range(26):
                if abs(prev - key) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[key] = max(dp[key], longest)
        
        return max(dp)
        