class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        inWindow = collections.defaultdict(int)

        l = 0
        longestSubstring = 0

        for r in range(len(s)):
            # add current char to window
            inWindow[s[r]] += 1

            # close window from left as long as we have > 2 of current char
            while inWindow[s[r]] > 2:
                inWindow[s[l]] -= 1
                l += 1
            
            longestSubstring = max(longestSubstring, r - l + 1)
        
        return longestSubstring