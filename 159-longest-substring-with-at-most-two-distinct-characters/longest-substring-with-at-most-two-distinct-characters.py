class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = collections.defaultdict(int)
        longest = 0
        l = 0

        for r in range(len(s)):

            seen[s[r]] += 1

            while len(seen) > 2:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                
                l += 1
            
            if len(seen) <= 2:
                longest = max(longest, r - l + 1)
        
        return longest

        