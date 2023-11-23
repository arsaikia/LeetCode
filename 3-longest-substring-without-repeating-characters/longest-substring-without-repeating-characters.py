class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = set()


        for r in range(len(s)):

            # close window
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # expand window
            seen.add(s[r])
            longest = max(longest, (r - l + 1))
        return longest
        