class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        inWindow = collections.defaultdict(int)

        l = 0
        res = 0

        for r in range(len(s)):
            inWindow[s[r]] += 1

            while inWindow[s[r]] > 2:
                inWindow[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res